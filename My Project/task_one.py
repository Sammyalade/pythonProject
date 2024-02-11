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
    total += lists[0]
    length_of_lists = len(lists)
    if len(lists) % 2 == 0:
        total += lists[length_of_lists / 2]
    else:
        total += (lists[length_of_lists // 2] + lists[(length_of_lists // 2) - 1]) / 2
    total += lists[length_of_lists - 1]

    return total


print(calculate_sum_of_last_middle_and_last_element(list1))
