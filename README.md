# Kumparan's NLP Services

`nlp-id` is a collection of modules which provides various functions for Natural Language Processing for Bahasa Indonesia. This repository contains all source code related to NLP services.

## Installation

To install `nlp-id`, use the following command:

    $ pip install nlp-id     


## Usage

Description on how to use the lemmatizer, tokenizer, POS-tagger, etc. will be explained in more detail in this section.

### Lemmatizer

Lemmatizer is used to get the root words from every word in a sentence.

    from nlp_id.lemmatizer import Lemmatizer 
    lemmatizer = Lemmatizer() 
    lemmatizer.lemmatize('Saya sedang mencoba') 
    # saya sedang coba 
    
### Tokenizer

Tokenizer is used to convert text into tokens of word, punctuation, number, date, email, URL, etc. 
There are two kinds of tokenizer in this repository, **standard tokenizer** and **phrase tokenizer**. 
The **standard tokenizer** tokenizes the text into separate tokens where the word tokens are single-word tokens.
Tokens that started with *ku-* or ended with *-ku*, *-mu*, *-nya*, *-lah*, *-kah* will be split if it is personal pronoun or particle.

    from nlp_id.tokenizer import Tokenizer 
    tokenizer = Tokenizer() 
    tokenizer.tokenize('Lionel Messi pergi ke pasar di daerah Jakarta Pusat.') 
    # ['Lionel', 'Messi', 'pergi', 'ke', 'pasar', 'di', 'daerah', 'Jakarta', 'Pusat', '.']

    tokenizer.tokenize('Lionel Messi pergi ke rumahmu di daerah Jakarta Pusat.') 
    # ['Lionel', 'Messi', 'pergi', 'ke', 'rumah', 'mu', 'di', 'daerah', 'Jakarta', 'Pusat', '.']
    
The **phrase tokenizer** tokenizes the text into separate tokens where the word tokens are phrases (single or multi-word tokens). 

    from nlp_id.tokenizer import PhraseTokenizer 
    tokenizer = PhraseTokenizer() 
    tokenizer.tokenize('Lionel Messi pergi ke pasar di daerah Jakarta Pusat.') 
    # ['Lionel Messi', 'pergi', 'ke', 'pasar', 'di', 'daerah', 'Jakarta Pusat', '.']
    
### POS Tagger

POS tagger is used to obtain the Part-Of-Speech tag from a text.
There are two kinds of POS tagger in this repository, **standard POS tagger** and **phrase POS tagger**. 
The tokens in **standard POS Tagger** are single-word tokens, while the tokens in **phrase POS Tagger** are phrases (single or multi-word tokens).

    from nlp_id.postag import PosTag
    postagger = PosTag() 
    postagger.get_pos_tag('Lionel Messi pergi ke pasar di daerah Jakarta Pusat.') 
    # [('Lionel', 'NNP'), ('Messi', 'NNP'), ('pergi', 'VB'), ('ke', 'IN'), ('pasar', 'NN'), ('di', 'IN'), ('daerah', 'NN'),  
      ('Jakarta', 'NNP'), ('Pusat', 'NNP'), ('.', 'SYM')]
    
    postagger.get_phrase_tag('Lionel Messi pergi ke pasar di daerah Jakarta Pusat.') 
    # [('Lionel Messi', 'NP'), ('pergi', 'VP'), ('ke', 'IN'), ('pasar', 'NN'), ('di', 'IN'), ('daerah', 'NN'), 
      ('Jakarta Pusat', 'NP'), ('.', 'SYM')]

    
Description of tagset used for POS Tagger:

| No. | Tag | Description | Example |
|:-----:|:-----:|:--------|:------------|
| 1 | ADV | Adverbs. Includes adverb, modal, and auxiliary verb | sangat, hanya, justru, boleh, harus, mesti|
| 2 | CC  | Coordinating conjunction. Coordinating conjunction links two or more syntactically equivalent parts of a sentence. Coordinating conjunction can link independent clauses, phrases, or words. | dan, tetapi, atau |
| 3 | DT  | Determiner/article. A grammatical unit which limits the potential referent of a noun phrase, whose basic role is to mark noun phrases as either definite or indefinite.| para, sang, si, ini, itu, nya |
| 4 | FW | Foreign word. Foreign word is a word which comes from foreign language and is not yet included in Indonesian dictionary| workshop, business, e-commerce |
| 5 | IN  | Preposition. A preposition links word or phrase and constituent in front of that preposition and results prepositional phrase. | dalam, dengan, di, ke|
| 6 | JJ | Adjective. Adjectives are words which describe, modify, or specify some properties of the head noun of the phrase | bersih, panjang, jauh, marah |
| 7 | NEG | Negation | tidak, belum, jangan |
| 8 | NN | Noun. Nouns are words which refer to human, animal, thing, concept, or understanding | meja, kursi, monyet, perkumpulan |
| 9 | NNP | Proper Noun. Proper noun is a specific name of a person, thing, place, event, etc. | Indonesia, Jakarta, Piala Dunia, Idul Fitri, Jokowi |
| 10 | NUM  | Number. Includes cardinal and ordinal number | 9876, 2019, 0,5, empat |
| 11 | PR  | Pronoun. Includes personal pronoun and demonstrative pronoun | saya, kami, kita, kalian, ini, itu, nya, yang |
| 12 | RP  | Particle. Particle which confirms interrogative, imperative, or declarative sentences | pun, lah, kah|
| 13 | SC  | Subordinating Conjunction. Subordinating conjunction links two or more clauses and one of the clauses is a subordinate clause. | sejak, jika, seandainya, dengan, bahwa |
| 14 | SYM | Symbols and Punctuations  | +,%,@ |
| 15 | UH | Interjection. Interjection expresses feeling or state of mind and has no relation with other words syntactically. | ayo, nah, ah|
| 16 | VB | Verb. Includes transitive verbs, intransitive verbs, active verbs, passive verbs, and copulas. | tertidur, bekerja, membaca |
| 17 | ADJP | Adjective Phrase. A group of words headed by an adjective that describes a noun or a pronoun | sangat tinggi |
| 18 | DP | Date Phrase. Date written with whitespaces | 1 Januari 2020 |
| 19 | NP | Noun Phrase. A phrase that has a noun (or indefinite pronoun) as its head | Jakarta Pusat, Lionel Messi |
| 20 | NUMP | Number Phrase.  | 10 juta |
| 21 | VP | Verb Phrase. A syntactic unit composed of at least one verb and its dependents | tidak makan |

### Stopword

`nlp-id` also provide list of Indonesian stopword.

    from nlp_id.stopword import StopWord 
    stopword = StopWord() 
    stopword.get_stopword() 
    # [{list_of_nlp_id_stopword}]    

Stopword Removal is used to remove every Indonesian stopword from the given text.

    from nlp_id.stopword import StopWord 
    text = "Lionel Messi pergi Ke pasar di area Jakarta Pusat" # single sentence
    stopword = StopWord() 
    stopword.remove_stopword(text)
    # Lionel Messi pergi pasar area Jakarta Pusat  
    
    paragraph = "Lionel Messi pergi Ke pasar di area Jakarta Pusat itu. Sedangkan Cristiano Ronaldo ke pasar Di area Jakarta Selatan. Dan mereka tidak bertemu begini-begitu."
    stopword.remove_stopword(text)
    # Lionel Messi pergi pasar area Jakarta Pusat. Cristiano Ronaldo pasar area Jakarta Selatan. bertemu.
    
## Training and Evaluation

Our model is trained using stories from kumparan as the dataset. We managed to get ~93% accuracy on our test set.
    
## Citation
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4556870.svg)](https://doi.org/10.5281/zenodo.4556870)
