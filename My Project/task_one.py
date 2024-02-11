list1 = list(range(1, 16))
print(list1)

duplicated_list = list1 + list1
print(duplicated_list)

transformed_list = list(set(duplicated_list))
print(transformed_list)


def add_every_third_element(lists) -> int:
    count = 1
    total = 0
    for element in lists:
        if count % 3 == 0:
            total += element
        count += 1

    return total


print(add_every_third_element(list1))


def calculate_sum_of_last_middle_and_last_element(lists) -> int:
    total = 0
    for number in range(len(lists)):
        if number == 1:
            total += lists[number - 1]
        if len(lists) - number == number:
            total += lists[number - 1]
        if len(lists) - number == number + 1:
            total += (lists[number + 1] + lists[number] / 2)
        if len(lists) - number == 0:
            total += lists[number - 1]

    return total


print(calculate_sum_of_last_middle_and_last_element(list1))
