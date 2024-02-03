list1 = [12, 45, 32, 2, 32, 23, 34, 12, 32, 12]


def get_length(lists) -> int:
    count = 0
    for item in lists:
        count += 1
    return count


def sum_element_in_even_position(lists) -> int:
    count = 0
    total = 0
    for item in lists:
        count += 1
        if count % 2 != 0:
            total += item
    return total


def sum_element_in_odd_position(lists) -> int:
    count = 0
    total = 0
    for item in lists:
        count += 1
        if count % 2 == 0:
            total += item
    return total


def multiply_elements_at_third_positions(lists) -> int:
    count = 0
    total = 1
    for item in lists:
        count += 1
        if count % 3 == 0:
            total *= item

    return total


def average_of_elements_in_the_list(lists) -> float:
    count = 0
    total = 0
    for item in lists:
        count += 1
        total += item
    return total / count


def largest_of_elements_in_the_list(lists) -> int:
    largest = 0
    for item in lists:
        if item > largest:
            largest = item
    return largest


def smallest_of_elements_in_the_list(lists) -> int:
    smallest = 0
    for item in range(len(lists)):
        if item == 0:
            smallest = lists[item]
        else:
            if lists[item] < smallest:
                smallest = lists[item]

    return smallest


list1 = ['gotten', 'go', 'len', 'get', 'give']


def check_strings_if_two_characters_are_the_same(lists) -> str:
    checker = ''
    for number in range(len(lists)):
        for item in lists:
            if len(item) > 1:
                if item[number] == lists[number][number]:
                    if number != len(lists) - 1:
                        if item[number+1] == lists[number][number+1]:
                            checker += item
    return checker


print(check_strings_if_two_characters_are_the_same(list1))

