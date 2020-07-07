from nlp_id.postag import PosTag

postagger = PosTag()


def test_pos_tag():
    """
    test for standard POS tagger
    """
    text = 'Lionel Messi pergi ke pasar di area Jakarta Pusat.'
    expected_result = [
        ('Lionel', 'NNP'),
        ('Messi', 'NNP'),
        ('pergi', 'VB'),
        ('ke', 'IN'),
        ('pasar', 'NN'),
        ('di', 'IN'),
        ('area', 'NN'),
        ('Jakarta', 'NNP'),
        ('Pusat', 'NNP'),
        ('.', 'SYM')
    ]

    assert postagger.get_pos_tag(text) == expected_result


def test_phrase_tag():
    """
    test for phrase POS tagger
    """
    text = 'Lionel Messi pergi ke pasar di area Jakarta Pusat.'
    expected_result =[
        ('Lionel Messi', 'NP'),
        ('pergi', 'VP'),
        ('ke', 'IN'),
        ('pasar', 'NN'),
        ('di', 'IN'),
        ('area', 'NN'),
        ('Jakarta Pusat', 'NP'),
        ('.', 'SYM')
    ]

    assert postagger.get_phrase_tag(text) == expected_result
