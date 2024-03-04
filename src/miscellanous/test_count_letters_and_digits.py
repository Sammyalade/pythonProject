import letters_and_digit


def test_count_letters_and_digits():
    assert letters_and_digit.count_letters_and_digits('hello world! 123') == {'LETTERS': 10,
                                                                              'DIGITS': 3}
