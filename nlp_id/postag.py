from nltk.tree import Tree
from nlp_id import tokenizer
import pickle
import os
import nltk

class PosTag:
    def __init__(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(current_dir, 'data', 'postagger.pkl')
        self.clf = self.load_model(model_path)
        self.tokenizer = tokenizer.Tokenizer()

    def load_model(self,model_path):
        pickle_in = open(model_path,"rb")
        load_data = pickle.load(pickle_in)
        return load_data

    def features(self, sentence, index):
        """ sentence: [w1, w2, ...], index: the index of the word """
        return {
            'word': sentence[index],
            'is_first': index == 0,
            'is_last': index == len(sentence) - 1,
            'is_capitalized': sentence[index][0].upper() == sentence[index][0],
            'is_all_caps': sentence[index].upper() == sentence[index],
            'is_all_lower': sentence[index].lower() == sentence[index],
            'has_hyphen': '-' in sentence[index],
            'is_numeric': sentence[index].isdigit(),
            'capitals_inside': sentence[index][1:].lower() != sentence[index][1:],
            'prefix-1': sentence[index][0],
            'prefix-1-lower': sentence[index][0].lower(),
            'prefix-2': sentence[index][:2],
            'prefix-2-lower': sentence[index][:2].lower(),
            'prefix-3': sentence[index][:3],
            'prefix-3-lower': sentence[index][:3].lower(),
            'suffix-1': sentence[index][-1],
            'suffix-1-lower': sentence[index][-1].lower(),
            'suffix-2': sentence[index][-2:],
            'suffix-2-lower': sentence[index][-2:].lower(),
            'suffix-3': sentence[index][-3:],
            'suffix-3-lower': sentence[index][-3:].lower(),
            'lowercase_word': sentence[index].lower(),
            'prev_word': '' if index == 0 else sentence[index - 1],
            'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        }

    def get_pos_tag(self, text):
        tokenized_word = self.tokenizer.tokenize(text)
        tags = self.clf.predict([self.features(tokenized_word, index) for index in range(len(tokenized_word))])
        result = []
        for i in range(len(tags)):
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
        chunk_rule = '''
            DP: {<NUM><NNP><NUM>}
            NP: {<NNP>+<CC><NNP>+}
            NP: {<NN>+<CC><NN>+}
            NP: {<FW>+}
            NP: {<NNP><NNP>+}
            NP: {<NN>+<JJ>}
            NP: {<NN><NN>+}
            NP: {<NP><NP>+}
            ADJP: {<JJ><ADV>}
            ADJP: {<ADV><JJ>}
            ADJP: {<JJ>+}
            ADJP: {<NEG>*<ADJP>}
            VP: {<NEG>*<VB>}
            '''
        chunkParser= nltk.RegexpParser(chunk_rule)
        tree = chunkParser.parse(tag)
        result = self.tree_to_list(tree)
        return result
    
    def get_phrase_tag(self,text):
        tag = self.get_pos_tag(text)
        phrase_tag = self.chunk_tag(tag)
        return phrase_tag
