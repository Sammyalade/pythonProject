def count_upper_and_lower_case(sentence):
    upper_case_count = 0
    lower_case_count = 0
    for char in sentence:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
    return {'UPPER CASE': upper_case_count, 'LOWER CASE': lower_case_count}


print(count_upper_and_lower_case('Hello world!'))


def count_upper_and_lower_case_two(sentence):
    return {'UPPER CASE': len(list(filter(lambda x: x.isupper(), sentence))),
            'LOWER CASE': len(list(filter(lambda x: x.islower(), sentence)))}


print(count_upper_and_lower_case('Hello world!'))
