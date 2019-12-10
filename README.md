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
    