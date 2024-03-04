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
