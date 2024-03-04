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


def count_letters_and_digits_two(sentence: str):
    letters = 0
    digits = 0
    for word in sentence:
        if word.isdigit():
            digits += 1
        elif word.isalpha():
            letters += 1
    return {"LETTERS": letters, "DIGITS": digits}


print(count_letters_and_digits_two("hello world! 123"))


def count_letters_and_digits_three(sentence: str):
    return {"LETTERS": len(list(filter(lambda letter: letter.isalpha(), sentence))),
            "DIGITS": len(list(filter(lambda letter: letter.isdigit(), sentence)))}


print(count_letters_and_digits_three("hello world! 123"))
