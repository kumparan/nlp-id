# Kumparan's NLP Services

`nlp-id` is a collection of modules which provides various functions for Natural Language Processing for Bahasa Indonesia. This repository contains all source code related to NLP services.

## Installation

To install `nlp-id`, use the following command:

    $ pip install nlp-id 
    
## Data

There are some data that needs to be downloaded before using the library:
1. [POS Tag model](https://storage.cloud.google.com/kumparan-public-bucket/nlp-id/postagger.pkl)

After downloading the data, you can place it inside the `nlp_id/data` folder.

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

    from nlp_id.tokenizer import Tokenizer 
    tokenizer = Tokenizer() 
    tokenizer.tokenize('Joko Widodo kembali terpilih menjadi presiden Republik Indonesia') 
    # ['Joko', 'Widodo', 'kembali', 'terpilih', 'menjadi', 'presiden', 'Republik', 'Indonesia'] 
    
The **phrase tokenizer** tokenizes the text into separate tokens where the word tokens are phrases (single or multi-word tokens). 

    from nlp_id.tokenizer import PhraseTokenizer 
    tokenizer = PhraseTokenizer() 
    tokenizer.tokenize('Joko Widodo kembali terpilih menjadi presiden Republik Indonesia') 
    # ['Joko Widodo', 'kembali', 'terpilih', 'menjadi', 'presiden', 'Republik Indonesia']
    
### POS Tagger

POS tagger is used to obtain the Part-Of-Speech tag from a text.
There are two kinds of POS tagger in this repository, **standard POS tagger** and **phrase POS tagger**. 
The tokens in **standard POS Tagger** are single-word tokens, while the tokens in **phrase POS Tagger** are phrases (single or multi-word tokens).

    from nlp_id.postag import PosTag
    postagger = PosTag() 
    postagger.get_pos_tag('Joko Widodo kembali terpilih menjadi presiden Republik Indonesia') 
    # [('Joko', 'NNP'), ('Widodo', 'NNP'), ('kembali', 'VB'), ('terpilih', 'VB'), ('menjadi', 'VB'), ('presiden', 'NN'),
      ('Republik', 'NNP'), ('Indonesia', 'NNP')]
    
    postagger.get_phrase_tag('Joko Widodo kembali terpilih menjadi presiden Republik Indonesia') 
    # [('Joko Widodo', 'NP'), ('kembali', 'VP'), ('terpilih', 'VP'), ('menjadi', 'VP'), ('presiden', 'NN'), 
      ('Republik Indonesia', 'NP')]
    
Description of tagset used for POS Tagger:
| No. | Tag | Description | Example |
|:-----:|:-----:|:--------|:------------|
| 1 | ADV | Adverbs. Includes adverb, modal, and auxiliary verb | sangat, hanya, justru, boleh, harus, mesti|
| 2 | CC  | Coordinating conjunction. Coordinating conjunction links two or more syntactically equivalent parts of a sentence. Coordinating conjunction can link independent clauses, phrases, or words. | dan, tetapi, atau |
| 3 | DT  | Determiner/article. A grammatical unit which limits the potential referent of a noun phrase, whose basic role is to mark noun phrases as either definite or indefinite.| para, sang, si |
| 4 | IN  | Preposition. A preposition links word or phrase and constituent in front of that preposition and results prepositional phrase. | dalam, dengan, di, ke|
| 5 | JJ | Adjective. Adjectives are words which describe, modify, or specify some properties of the head noun of the phrase | bersih, panjang, jauh, marah |
| 6 | NEG | Negation | tidak, belum, jangan |
| 7 | NN | Noun. Nouns are words which refer to human, animal, thing, concept, or understanding | meja, kursi, monyet, perkumpulan |
| 8 | NNP | Proper Noun. Proper noun is a specific name of a person, thing, place, event, etc. | Indonesia, Jakarta, Piala Dunia, Idul Fitri, Jokowi |
| 9 | NUM  | Number. Includes cardinal and ordinal number | 9876, 2019, 0,5, empat |
| 10 | PR  | Pronoun. Includes personal pronoun and demonstrative pronoun | saya, kami, kita, kalian, ini, itu |
| 11 | RP  | Particle. Particle which confirms interrogative, imperative, or declarative sentences | pun, lah, kah|
| 12 | SC  | Subordinating Conjunction. Subordinating conjunction links two or more clauses and one of the clauses is a subordinate clause. | sejak, jika, seandainya, dengan, bahwa, yang|
| 13 | SYM | Symbols and Punctuations  | +,%,@ |
| 14 | UH | Interjection. Interjection expresses feeling or state of mind and has no relation with other words syntactically. | ayo, mari, aduh|
| 15 | VB | Verb. Includes transitive verbs, intransitive verbs, active verbs, passive verbs, and copulas. | tertidur, bekerja, membaca |
| 16 | WH | Question words | siapa, apa, kapan, bagaimana |