from nlp_id.tokenizer import Tokenizer, PhraseTokenizer


def test_tokenizer():
    """
    test for Tokenizer
    """
    tokenizer = Tokenizer()
    text = 'Lionel Messi pergi ke pasar di area Jakarta Pusat.'
    expected_result = [
        'Lionel',
        'Messi',
        'pergi',
        'ke',
        'pasar',
        'di',
        'area',
        'Jakarta',
        'Pusat',
        '.'
    ]
    assert tokenizer.tokenize(text) == expected_result


def test_phrase_tokenizer():
    """
    test for PhraseTokenizer
    """
    phrase_tokenizer = PhraseTokenizer()
    text = 'Lionel Messi pergi ke pasar di area Jakarta Pusat.'
    expected_result = [
        'Lionel Messi',
        'pergi',
        'ke',
        'pasar',
        'di',
        'area',
        'Jakarta Pusat',
        '.'
    ]

    assert phrase_tokenizer.tokenize(text) == expected_result
