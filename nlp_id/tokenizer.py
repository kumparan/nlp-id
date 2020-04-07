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
        text = re.sub("\u2014|\u2013", "-", text)
        text = re.sub("\u2018|\u2019", "'", text)
        text = re.sub("\u201c|\u201d", '"', text)
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
        if "@" in word:
            if re.search(
                "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", word
            ):
                return True

            else:
                return False

    def normalize_word(self, word):
        normalized_word = ""
        should_join = False
        for i in self.inside_punct:
            if i in word:
                normalized_word = word.split(i)
                break
        # handling punctuations
        if i in ["/"]:
            count = 0
            for each in normalized_word:
                if not each.isdigit():
                    count += 1
            if count < len(normalized_word):
                should_join = True

        if i in ["'"]:
            count = 0
            for each in normalized_word:
                if not each.isalpha():
                    count += 1
            if count < len(normalized_word):
                should_join = True

        if i in [".", ","]:
            pre_norm_word = []
            text = ""
            for j in range(len(normalized_word)):
                if normalized_word[j].isdigit():
                    if not text:
                        text = normalized_word[j]
                    else:
                        text += i + normalized_word[j]
                else:
                    pre_norm_word.append(text)
                    text = ""
                    pre_norm_word.append(normalized_word[j])
            if normalized_word[j].isdigit():
                pre_norm_word.append(normalized_word[j])
            normalized_word = [word for word in pre_norm_word if word]
            count = 0
            for each in normalized_word:
                if not each.isdigit():
                    count += 1
            if count == 0:
                should_join = True

        if normalized_word:
            for j in range(len(normalized_word) - 2, -1, -1):
                normalized_word.insert(j + 1, i)
            normalized_word = [i for i in normalized_word if i]
        else:
            normalized_word = [word]

        if should_join:
            normalized_word = ["".join(normalized_word)]

        return normalized_word

    def tokenize(self, text):
        text = self.convert_non_ascii(text)
        if len(text) == 1:
            return [text]
        splitted_text = text.split()
        tokens = []
        for word in splitted_text:
            start_token = []
            end_token = []

            for i in range(len(word)):
                if word[i] in self.outside_punct:
                    start_token.append(word[i])
                else:
                    break
            for j in range((len(word) - 1), -1, -1):
                if word[j] in self.outside_punct:
                    end_token.insert(0, word[j])
                else:
                    break
            token = word[i:j+1]
            if not self.is_url(token) and not self.is_email(token):

                token_word = self.normalize_word(token)
            else:
                token_word = [token]

            # for handling word like "......." or ",,,,"
            if token_word == [""]:
                token_word = []
                end_token = []
            tokens += start_token + token_word + end_token
        return tokens


class PhraseTokenizer:
    def __init__(self):
        self.postagger = postag.PosTag()

    def tokenize(self, text):
        phrase_tag = self.postagger.get_phrase_tag(text)
        tokens = [phrase[0] for phrase in phrase_tag]
        return tokens
