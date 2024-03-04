def count_letters_and_digits(sentence: str):
    letters = 0
    digits = 0
    for word in sentence:
        if word.isdigit():
            digits += 1
        elif word.isalpha():
            letters += 1
    return f"LETTERS {letters}, DIGITS {digits}"


print(count_letters_and_digits("hello world! 123"))


def count_letters_and_digitsTwo(sentence: str):
    letters = 0
    digits = 0
    for word in sentence:
        if word.isdigit():
            digits += 1
        elif word.isalpha():
            letters += 1
    return {"LETTERS": letters, "DIGITS": digits}


print(count_letters_and_digitsTwo("hello world! 123"))
