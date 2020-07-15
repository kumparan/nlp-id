import os


class StopWord:
    def __init__(self, stopword_path=None):
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        if not stopword_path:
            stopword_path = os.path.join(
                self.current_dir, "data", "stopword.txt"
            )
        with open(stopword_path) as f:
            self.stopwords = f.read().split('\n')

    def get_stopword(self):
        return self.stopwords

    def remove_stopword(self, text):
        given_words = text.split(' ')
        stopword = self.get_stopword()
        result = []
        for word in given_words:
            if word.casefold() not in stopword:
                result.append(word)

        return ' '.join(result)
