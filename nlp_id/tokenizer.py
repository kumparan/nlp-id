import os
import re
from nlp_id import Lemmatizer, postag


class Tokenizer:
    def __init__(self):
        self.start_url = ["www.", "http"]
        self.end_url = [".com", ".id", ".io", ".html", ".org", ".net"]
        self.inside_punct = ['!', '&', '(', ')', '*', '?', ',', '.', '<', '>', '/', ':', ';',
                             '[', ']', '\\', '^', '`', '{', '}', '|', '~', '"', '“', "'"]
        self.outside_punct = self.inside_punct + ["-", "_"]
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.lemmatizer = Lemmatizer()
        CliticsFile = os.path.join(self.current_dir, "data", "non_clitics.txt")
        with open(CliticsFile) as f:
            self.non_clitics = set(f.read().splitlines())

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
                if len(normalized_word)-1 == j:
                    pre_norm_word.append(text)

            normalized_word = [word for word in pre_norm_word if word]
            count = 0
            check = 0
            index_tobe_popped = 0
            new_word = ""
            for each in normalized_word:
                if i == ".":
                    if each.isalpha():
                        count += 1
                    elif not each.isdigit():
                        if check > 0 or \
                                (normalized_word[check-1].isdigit() or
                                 normalized_word[check-1].isalpha()):
                            new_word = normalized_word[check-1] + i + each
                            index_tobe_popped = check
                    check += 1
                else:
                    if not each.isdigit():
                        count += 1
            if index_tobe_popped > 0:
                normalized_word.pop(index_tobe_popped)
                normalized_word.pop(index_tobe_popped-1)
                normalized_word.insert(index_tobe_popped-1, new_word)
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

    def clitic_tokenize(self, word):
        tokens = []
        start_clitic = ("ku", "Ku")
        end_clitic = ("ku", "mu", "Ku", "Mu")
        end_clitic2 = ("-ku", "-mu", "-Ku", "-Mu", "Nya", "nya", "lah", "kah")
        end_clitic3 = ("-Nya", "-nya")
        end_clitic4 = ("-kulah", "-mulah", "-nyalah")
        if (
            not word.startswith(start_clitic)
            and not word.endswith(end_clitic)
            and not word.endswith(end_clitic2)
        ):
            tokens += [word]
        elif word.lower() not in self.non_clitics:
            lemma = self.lemmatizer.lemmatize(word)
            if lemma != word.lower() or lemma.endswith(end_clitic4):
                if word.startswith(start_clitic):
                    new_lemma = self.lemmatizer.lemmatize(word[2:])
                    if new_lemma == lemma:
                        tokens += [word[:2]]
                        word = word[2:]
                        if not word.endswith(
                            end_clitic
                        ) and not word.endswith(end_clitic2):
                            tokens += [word]
                    elif not word.endswith(
                        end_clitic
                    ) and not word.endswith(end_clitic2):
                        tokens += [word]
                if word.endswith(end_clitic3):
                    tokens += [word[:-4], word[-4:]]
                elif word.endswith(end_clitic2):
                    new_lemma = self.lemmatizer.lemmatize(word[:-3])
                    if new_lemma == lemma or word[:-3].endswith(
                        ("-ku", "-Ku", "-mu", "-Mu", "-nya", "-Nya")
                    ):
                        if word[:-3].endswith(end_clitic3):
                            tokens += [word[:-3][:-4], word[:-3][-4:], word[-3:]]
                        elif word[:-3].endswith(end_clitic2):
                            new_lemma2 = self.lemmatizer.lemmatize(word[:-3][:-3])
                            if new_lemma2 == new_lemma:
                                tokens += [word[:-3][:-3], word[:-3][-3:], word[-3:]]
                            elif (
                                word[:-3].startswith(("se", "Se")) 
                                and self.lemmatizer.lemmatize(word[:-3][2:]) == new_lemma
                            ):
                                tokens += [word]
                            else:
                                tokens += [word[:-3], word[-3:]]
                        elif word[:-3].endswith(end_clitic):
                            new_lemma2 = self.lemmatizer.lemmatize(word[:-3][:-2])
                            if new_lemma2 == new_lemma:
                                tokens += [word[:-3][:-2], word[:-3][-2:], word[-3:]]
                            else:
                                tokens += [word[:-3], word[-3:]]
                        elif (
                            word.startswith(("se", "Se"))
                            and word.endswith("nya")
                            and self.lemmatizer.lemmatize(word[2:]) == lemma
                        ):
                            tokens += [word]
                        else:
                            tokens += [word[:-3], word[-3:]]
                    else:
                        tokens += [word]
                elif word.endswith(end_clitic):
                    new_lemma = self.lemmatizer.lemmatize(word[:-2])
                    if new_lemma == lemma:
                        tokens += [word[:-2], word[-2:]]
                    else:
                        tokens += [word]
            else:
                tokens += [word]
        else:
            tokens += [word]
        return tokens

    def tokenize(self, text):
        text = self.convert_non_ascii(text)
        if len(text) == 1:
            return [text]
        splitted_text = text.split()
        tokens = []
        for word in splitted_text:
            if len(word) == 1:
                tokens += word
            else:
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
                    norm_word = self.normalize_word(token)
                    token_word = []
                    for word in norm_word:
                        token_word += self.clitic_tokenize(word)
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
