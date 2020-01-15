import re
from nlp_id import postag


class Tokenizer:
    def __init__(self):
        self.start_url = ["www.", "http"]
        self.end_url = [".com", ".id", ".io", ".html", ".org", ".net"]
        self.inside_punct = ['!', '&', '(', ')', '*', '?', ',', '.', '<', '>', '/', ':', ';',
                      '[', ']', '\\', '^', '`', '{', '}', '|', '~', '"', '“', "'"]
        self.outside_punct = self.inside_punct + ["-", "_"]

    def convert_non_ascii(self, text):
        text = re.sub('\u2014|\u2013', '-', text)
        text = re.sub('\u2018|\u2019', "'", text)
        text = re.sub('\u201c|\u201d', '"', text)
        return text

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
        check = False
        check2 = False
        check3 = False
        for i in self.inside_punct:
            if i in word:
                normalized_word = word.split(i)
                break
        # handling / or .
        if i in ["/"]:
            count = 0
            for each in normalized_word:
                if not each.isdigit():
                    count += 1
            if count < len(normalized_word):
                check = True

        if i in ["'"]:
            count = 0
            for each in normalized_word:
                if not each.isalpha():
                    count += 1
            if count < len(normalized_word):
                check2 = True
                
        if i in [".",","]:
            fin = []
            text = ""
            for j in range(len(normalized_word)):
                if normalized_word[j].isdigit():
                    if not text:
                        text = normalized_word[j]
                    else:
                        text += i + normalized_word[j]
                else:
                    fin.append(text)
                    text = ""
                    fin.append(normalized_word[j])
            if normalized_word[j].isdigit():
                fin.append(normalized_word[j])
            normalized_word = [x for x in fin if x]
            count = 0
            for each in normalized_word:
                if not each.isdigit():
                    count += 1
            if count == 0:
                check3 = True

        if normalized_word :
            for j in range(len(normalized_word) - 2, -1, -1):
                normalized_word.insert(j + 1, i)
            normalized_word = [i for i in normalized_word if i]
        else:
            normalized_word = [word]

        if check or check2 or check3:
            normalized_word = ["".join(normalized_word)]

        return normalized_word

    def tokenize(self, text):
        text = self.convert_non_ascii(text)
        if len(text) == 1:
            return [text]
        splitted_text = text.split()
        final = []
        for kata in splitted_text:
            awal = []
            akhir = []

            for i in range(len(kata)):
                if kata[i] in self.outside_punct:
                    awal.append(kata[i])
                else:
                    break
            for j in range((len(kata) - 1), -1, -1):
                if kata[j] in self.outside_punct:
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

class PhraseTokenizer:
    def __init__(self):
        self.postagger = postag.PosTag()
    
    def tokenize(self, text):
        phrase_tag = self.postagger.get_phrase_tag(text)
        tokens = [phrase[0] for phrase in phrase_tag]
        return tokens
