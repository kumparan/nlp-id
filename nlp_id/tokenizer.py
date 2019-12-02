import re

class Tokenizer:
    def __init__(self):
        self.start_url = ["www.", "http"]
        self.end_url = [".com", ".id", ".io", ".html", ".org", ".net"]
        self.punct = ['!', '&', '(', ')', '*', '?', ',', '.', '<', '>', '/', ':', ';',
                      '[', ']', '\\', '^', '`', '{', '}', '|', '~', '"', '“']

    def is_url(self, word):

        if any(word.startswith(i) for i in self.start_url):
            return True

        if any(word.endswith(i) for i in self.end_url):
            return True

        updated_end = [i + "/" for i in self.end_url]

        if any(i in word for i in updated_end):
            return True

        return False

    def is_email(self, kata):
        if ("@" in kata):
            if (re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', kata)):
                return True

            else:
                return False

    def normalize_word(self, word, punct):
        normalize_word = ""
        for i in punct:
            if i in word:
                normalize_word = word.split(i)
                break
        if normalize_word != "":
            for j in range(len(normalize_word) - 2, -1, -1):
                normalize_word.insert(j + 1, i)

            normalize_word = [i for i in normalize_word if i is not ""]

        else:
            normalize_word = [word]
        return normalize_word

    def tokenize_postag(self, text):
        split_text = text.split()
        final = []
        for kata in split_text:
            awal = []
            akhir = []

            for i in range(len(kata)):
                if kata[i] in self.punct:
                    awal.append(kata[i])
                else:
                    break
            if (i != len(kata)-1):
                for j in range((len(kata) - 1), -1, -1):
                    if kata[j] in self.punct:
                        akhir.insert(0, kata[j])
                    else:
                        break
                tengah = kata[i:j+1]
                if (not self.is_url(tengah) and not self.is_email(tengah)):

                    kata_tengah = self.normalize_word(tengah, self.punct)
                else:
                    kata_tengah = [tengah]
            else:
                kata_tengah = []
                akhir = []

            final += awal + kata_tengah + akhir
        return final