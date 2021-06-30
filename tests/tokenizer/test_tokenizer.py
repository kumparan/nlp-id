from nlp_id.tokenizer import Tokenizer, PhraseTokenizer


def test_tokenizer():
    """
    test for Tokenizer
    """
    tokenizer = Tokenizer()
    text = "Lionel Messi pergi ke pasar di area Jakarta Pusat."
    text2 = (
        "Pada akhirnya, kucobalah apakah benar masakanmu enaknya seperti yang kukira."
    )
    text3 = "semuanya pemukulnya adalah kamulah kepadamulah inilah siapakah sepatutnya temukanlah kumenemukanmu kumenemukannya nyonya nyonyamu"
    text4 = "kemauanmu terakhirku miliknya pemiliknya kupukul dipukul"
    res = [
        "Lionel",
        "Messi",
        "pergi",
        "ke",
        "pasar",
        "di",
        "area",
        "Jakarta",
        "Pusat",
        ".",
    ]
    res2 = [
        "Pada",
        "akhirnya",
        ",",
        "ku",
        "coba",
        "lah",
        "apakah",
        "benar",
        "masakan",
        "mu",
        "enak",
        "nya",
        "seperti",
        "yang",
        "ku",
        "kira",
        ".",
    ]
    res3 = [
        "semua",
        "nya",
        "pemukul",
        "nya",
        "adalah",
        "kamu",
        "lah",
        "kepada",
        "mu",
        "lah",
        "ini",
        "lah",
        "siapa",
        "kah",
        "sepatutnya",
        "temukan",
        "lah",
        "ku",
        "menemukan",
        "mu",
        "ku",
        "menemukan",
        "nya",
        "nyonya",
        "nyonya",
        "mu",
    ]
    res4 = [
        "kemauan",
        "mu",
        "terakhir",
        "ku",
        "milik",
        "nya",
        "pemilik",
        "nya",
        "ku",
        "pukul",
        "dipukul",
    ]
    assert tokenizer.tokenize(text) == res
    assert tokenizer.tokenize(text2) == res2
    assert tokenizer.tokenize(text3) == res3
    assert tokenizer.tokenize(text4) == res4


def test_phrase_tokenizer():
    """
    test for PhraseTokenizer
    """
    phrase_tokenizer = PhraseTokenizer()
    text = "Lionel Messi pergi ke pasar di area Jakarta Pusat."
    expected_result = [
        "Lionel Messi",
        "pergi",
        "ke",
        "pasar",
        "di",
        "area",
        "Jakarta Pusat",
        ".",
    ]

    assert phrase_tokenizer.tokenize(text) == expected_result
