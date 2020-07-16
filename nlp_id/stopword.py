import os
import re

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
        stopword = self.get_stopword()
        temp_result = []
        parts = []

        for match in re.finditer(r'[^.,?!\s]+|[.,?!]', text):
            parts.append(match.group())

        for word in parts:
            if word.casefold() not in stopword:
                temp_result.append(word)

        result_cand = ' '.join(temp_result)
        result = re.sub(r' ([^A-Za-z0-9])', r'\1', result_cand)

        return result
