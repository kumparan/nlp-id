from tokenizer import Tokenizer
import pickle

class Postag:
    def __init__(self, model_path):
        self.clf = self.load_model(model_path)

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
            'prefix-2': sentence[index][:2],
            'prefix-3': sentence[index][:3],
            'suffix-1': sentence[index][-1],
            'suffix-2': sentence[index][-2:],
            'suffix-3': sentence[index][-3:],
            'lowercase_word': sentence[index].lower(),
            'prev_word': '' if index == 0 else sentence[index - 1],
            'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        }

    def predict(self, text):
        tokenized_word = Tokenizer.tokenize_postag(text)

        tags = self.clf.predict([self.features(tokenized_word, index) for index in range(len(tokenized_word))])
        temp = []
        for i in range(len(tags)):
            temp.append((tokenized_word[i], tags[i]))
        return temp
