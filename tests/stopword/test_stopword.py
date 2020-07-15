from nlp_id.stopword import StopWord


def test_stopword():
    """
    test for stopwords
    """
    number_of_nlp_id_stopword = 1168
    stopword = StopWord()
    stopword = stopword.get_stopword()
    assert len(stopword) == number_of_nlp_id_stopword


def test_remove_stopword():
    text = "Lionel Messi pergi Ke pasar di area Jakarta Pusat."
    stopword = StopWord()
    x = stopword.remove_stopword(text)
    print(x)
    expected_result = "Lionel Messi pergi pasar area Jakarta Pusat."
    assert stopword.remove_stopword(text) == expected_result
