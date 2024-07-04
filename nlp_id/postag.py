import nltk
import os
import pickle
import logging
from huggingface_hub import hf_hub_download
from nlp_id import tokenizer
from nltk.tree import Tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline


class PosTag:
    def __init__(self, model_path=None):
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        if not model_path:
            folder_name = "data"
            repo_id = "kumparanai/postagger"
            file_name = "postagger_v10.pkl"

            folder_path = os.path.join(self.current_dir, folder_name)
            model_path = os.path.join(folder_path, file_name)

            if not os.path.isfile(model_path):
                listdir_data = os.listdir(folder_path)
                # Find any file which ends with .pkl
                all_pickle = [
                    os.path.join(folder_path, file_path)
                    for file_path in listdir_data
                    if file_path.endswith(".pkl")
                    and file_path.startswith("postagger")
                ]
                # Remove all .pkl file
                if all_pickle:
                    for pickle_file in all_pickle:
                        os.remove(pickle_file)
                        logging.info("Removed", pickle_file)
                else:
                    logging.info("No model removed")
                logging.info("Downloading model ..")
                model_path = hf_hub_download(repo_id=repo_id, filename=file_name)
        self.clf = self.load_model(model_path)
        self.tokenizer = tokenizer.Tokenizer()

    def load_model(self, model_path):
        pickle_in = open(model_path, "rb")
        load_data = pickle.load(pickle_in)
        return load_data

    def features(self, sentence, index):
        """ sentence: [w1, w2, ...], index: the index of the word """
        return {
            "word": sentence[index],
            "is_first": index == 0,
            "is_last": index == len(sentence) - 1,
            "is_capitalized": sentence[index][0].upper()
            == sentence[index][0],
            "is_all_caps": sentence[index].upper() == sentence[index],
            "is_all_lower": sentence[index].lower() == sentence[index],
            "has_hyphen": "-" in sentence[index],
            "is_numeric": sentence[index].isdigit(),
            "capitals_inside": sentence[index][1:].lower()
            != sentence[index][1:],
            "prefix-1": sentence[index][0],
            "prefix-1-lower": sentence[index][0].lower(),
            "prefix-2": sentence[index][:2],
            "prefix-2-lower": sentence[index][:2].lower(),
            "prefix-3": sentence[index][:3],
            "prefix-3-lower": sentence[index][:3].lower(),
            "suffix-1": sentence[index][-1],
            "suffix-1-lower": sentence[index][-1].lower(),
            "suffix-2": sentence[index][-2:],
            "suffix-2-lower": sentence[index][-2:].lower(),
            "suffix-3": sentence[index][-3:],
            "suffix-3-lower": sentence[index][-3:].lower(),
            "lowercase_word": sentence[index].lower(),
            "prev_word": "" if index == 0 else sentence[index - 1],
            "next_word": ""
            if index == len(sentence) - 1
            else sentence[index + 1],
            "prev_word_is_capitalized": False
            if index == 0
            else sentence[index - 1][0].upper() == sentence[index - 1][0],
            "next_word_is_capitalized": False
            if index == len(sentence) - 1
            else sentence[index + 1][0].upper() == sentence[index + 1][0],
            "2-prev-word": "" if index <= 1 else sentence[index - 2],
            "2-next-word": ""
            if index >= len(sentence) - 2
            else sentence[index + 2],
        }

    def get_pos_tag(self, text):
        result = []
        sents = nltk.sent_tokenize(text)
        symbols = ['!', '&', '(', ')', '*', '?', ',', '.', '<', '>', '/', ':', ';',
                   '[', ']', '\\', '^', '`', '{', '}', '|', '~', '"', '“', "'"]
        for sent in sents:
            tokenized_word = self.tokenizer.tokenize(sent)
            if sent:
                tags = self.clf.predict(
                    [
                        self.features(tokenized_word, index)
                        for index in range(len(tokenized_word))
                    ]
                )
                for i in range(len(tags)):
                    if tokenized_word[i] in symbols:
                        result.append((tokenized_word[i], "SYM"))
                    else:
                        result.append((tokenized_word[i], tags[i]))
        return result

    def tree_to_list(self, tree_data):
        result = []
        for subtree in tree_data:
            if type(subtree) == Tree:
                phrase = " ".join([token for token, pos in subtree.leaves()])
                result.append((phrase, subtree.label()))
            else:
                result.append((subtree[0], subtree[1]))
        return result

    def chunk_tag(self, tag):
        chunk_rule = """
            DP: {<NUM><NNP><NUM>}
            NP: {<NNP><NNP>+}
            NP: {<NN>+<JJ>}
            NP: {<FW><FW>+}
            NP: {<NP><NP>+}
            ADJP: {<JJ><ADV>}
            ADJP: {<ADV><JJ>}
            ADJP: {<JJ>+}
            ADJP: {<NEG>*<ADJP>}
            VP: {<NEG>*<VB>}
            NUMP: {<NUM><NUM>+}
            """
        chunkparser = nltk.RegexpParser(chunk_rule)
        tree = chunkparser.parse(tag)
        result = self.tree_to_list(tree)
        return result

    def get_phrase_tag(self, text):
        if text:
            tag = self.get_pos_tag(text)
            phrase_tag = self.chunk_tag(tag)
        else:
            phrase_tag = []
        return phrase_tag

    def read_dataset(self, dataset_path=None):
        if not dataset_path:
            dataset_path = os.path.join(
                self.current_dir, "data", "dataset_postag.txt"
            )

        with open(dataset_path) as f:
            raw_file = f.read().split("\n")

        files = [i.split("\t") for i in raw_file]

        sentences, tags, temp_sentences, temp_tags = [], [], [], []

        for file in files:
            if file != [""]:
                temp_sentences.append(file[0])  # get the sentences
                temp_tags.append(file[1])  # get the tag
            else:
                # check if the temp sentences and temp tags is not null
                # and both of them have the same length
                if len(temp_sentences) > 0 and (
                    len(temp_sentences) == len(temp_tags)
                ):
                    sentences.append(temp_sentences)
                    tags.append(temp_tags)
                temp_sentences, temp_tags = [], []
        return sentences, tags

    def transform_to_dataset(self, sentences, tags):
        X, y = [], []

        for sentence_idx in range(len(sentences)):
            for index in range(len(sentences[sentence_idx])):
                X.append(self.features(sentences[sentence_idx], index))
                y.append(tags[sentence_idx][index])

        return X, y

    def train(self, sentences, tags):
        self.clf = Pipeline(
            [
                ("vectorizer", DictVectorizer(sparse=True)),
                (
                    "classifier",
                    RandomForestClassifier(
                        criterion="gini", n_estimators=15, random_state=2020
                    ),
                ),
            ]
        )

        self.clf.fit(sentences, tags)

    def save_model(self, model_path):
        pickle_out = open(model_path, "wb")
        pickle.dump(self.clf, pickle_out)
        pickle_out.close()
