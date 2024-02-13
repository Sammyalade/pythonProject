import swap_character


def test_swap_character():
    assert swap_character.swap("abcd", "xyzq") == "xyzd abcq"


def test_swap_case():
    assert swap_character.swap_second_try("abcd", "xyzq") == "xyzd abcq"
