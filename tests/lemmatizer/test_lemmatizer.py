from nlp_id.lemmatizer import Lemmatizer


def test_lemmatizer():
    """
    test for Lemmatizer
    """
    lemmatizer = Lemmatizer()
    text = 'Saya sedang mencoba'
    expected_result = 'saya sedang coba'

    assert lemmatizer.lemmatize(text) == expected_result
