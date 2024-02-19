def get_length(self):
    count = 0
    for item in self:
        count += 1
    return count


def sum_of_element_in_even_position(self) -> int:
    count = 0
    total = 0
    for item in self:
        count += 1
        if count % 2 != 0:
            total += item
    return total


def sum_of_element_in_odd_position(self) -> int:
    count = 0
    total = 0
    for item in self:
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
