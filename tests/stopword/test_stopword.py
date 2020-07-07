from nlp_id.stopword import StopWord


def test_stopword():
    """
    test for stopwords
    """
    number_of_nlp_id_stopword = 1168
    stopword = StopWord()
    stopword = stopword.get_stopword()
    assert len(stopword) == number_of_nlp_id_stopword
