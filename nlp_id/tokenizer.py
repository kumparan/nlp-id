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

    def is_email(self, word):
        if ("@" in word):
            if (re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', word)):
                return True

            else:
                return False

    def normalize_word(self, word):
        normalized_word = ""
        for i in self.punct:
            if i in word:
                normalized_word = word.split(i)
                break
        if normalized_word :
            for j in range(len(normalized_word) - 2, -1, -1):
                normalized_word.insert(j + 1, i)

            normalized_word = [i for i in normalized_word if i]

        else:
            normalized_word = [word]
        return normalized_word

    def tokenize_postag(self, text):
        splitted_text = text.split()
        final = []
        for kata in splitted_text:
            awal = []
            akhir = []

            for i in range(len(kata)):
                if kata[i] in self.punct:
                    awal.append(kata[i])
                else:
                    break
            for j in range((len(kata) - 1), -1, -1):
                if kata[j] in self.punct:
                    akhir.insert(0, kata[j])
                else:
                    break
            tengah = kata[i:j+1]
            if (not self.is_url(tengah) and not self.is_email(tengah)):

                kata_tengah = self.normalize_word(tengah)
            else:
                kata_tengah = [tengah]

            # for handling word like "......." or ",,,,"
            if kata_tengah == [""]:
                kata_tengah = []
                akhir = []

            final += awal + kata_tengah + akhir
        return final
