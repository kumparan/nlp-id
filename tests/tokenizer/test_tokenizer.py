from nlp_id.tokenizer import Tokenizer, PhraseTokenizer


def test_tokenizer():
    """
    test for Tokenizer
    """
    tokenizer = Tokenizer()
    text = "Lionel Messi pergi ke pasar di area Jakarta Pusat."
    text2 = "Pada akhirnya, kucobalah apakah benar masakanmu enaknya seperti yang kukira."
    text3 = "semuanya pemukulnya adalah kamulah kepadamulah inilah siapakah sepatutnya temukanlah kumenemukanmu kumenemukannya nyonya nyonyamu nyonyaMu nyonya-mu nyonya-Mu nyonyaku nyonya-Ku nyonyanya kumparan kepadanyalah kepada-Mulah kepada-Nyalah secepat-cepatnya sendoknya semestinya sepenuhnya setelahnya sebelum-sebelumnya setelah-setelahnya kata-katanya angan-anganku kupikir-pikir kulkasku kulkas-kulkasku kulkas"
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
        "semuanya",
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
        "nyonya",
        "Mu",
        "nyonya",
        "-mu",
        "nyonya",
        "-Mu",
        "nyonya",
        "ku",
        "nyonya",
        "-Ku",
        "nyonya",
        "nya",
        "kumparan",
        "kepada",
        "nya",
        "lah",
        "kepada",
        "-Mu",
        "lah",
        "kepada",
        "-Nya",
        "lah",
        "secepat-cepatnya",
        "sendok",
        "nya",
        "semestinya",
        "sepenuhnya",
        "setelahnya",
        "sebelum-sebelumnya",
        "setelah-setelahnya",
        "kata-kata",
        "nya",
        "angan-angan",
        "ku",
        "ku",
        "pikir-pikir",
        "kulkas",
        "ku",
        "kulkas-kulkas",
        "ku",
        "kulkas",
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
