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