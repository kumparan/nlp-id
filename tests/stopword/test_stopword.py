from nlp_id.stopword import StopWord


def test_stopword():
    """
    test for stopwords
    """
    number_of_nlp_id_stopword = 1168
    stopword = StopWord()
    stopword = stopword.get_stopword()
    assert len(stopword) == number_of_nlp_id_stopword


def test_remove_stopword_single_sentence():
    """
    test remove stopwords in single sentence
    """
    text = "Lionel Messi pergi Ke pasar di area Jakarta Pusat itu"
    stopword = StopWord()
    expected_result = "Lionel Messi pergi pasar area Jakarta Pusat"
    assert stopword.remove_stopword(text) == expected_result


def test_remove_stopword_paragragph():
    """
    test remove stopwords in paragraph
    """
    text = "Lionel Messi pergi Ke pasar di area Jakarta Pusat itu. " \
           "Sedangkan Cristiano Ronaldo ke pasar Di area Jakarta Selatan. Dan mereka tidak bertemu begini-begitu."
    stopword = StopWord()
    expected_result = "Lionel Messi pergi pasar area Jakarta Pusat. " \
                      "Cristiano Ronaldo pasar area Jakarta Selatan. bertemu."
    assert stopword.remove_stopword(text) == expected_result
