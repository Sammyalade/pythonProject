def check_for_a_number(numbers, key):
    for number in range(len(numbers)):
        if numbers[number] == key:
            return f"{number}"


print(check_for_a_number([10, 9, 8, 5, 4, 3, 2, 1], 1))

