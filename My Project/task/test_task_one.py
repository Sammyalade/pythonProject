import task_one


def test_get_length():
    assert task_one.get_length([12, 45, 32, 2, 32, 23, 34, 12, 32, 12]) == 10


def test_sum_element_in_even_position():
    assert task_one.sum_element_in_even_position([12, 45, 32, 2, 32, 23, 34, 12, 32, 12]) == 142


def test_sum_element_in_odd_position():
    assert task_one.sum_element_in_odd_position([12, 45, 32, 2, 32, 23, 34, 12, 32, 12]) == 94


def multiply_elements_at_third_positions():
    assert task_one.multiply_elements_at_third_positions([12, 45, 32, 2, 32, 23, 34, 12, 32, 12]) == 87


def average_of_elements_in_the_list():
    assert task_one.average_of_elements_in_the_list([12, 45, 32, 2, 32, 23, 34, 12, 32, 12]) == 23.6


def test_largest_of_elements_in_the_list():
    assert task_one.largest_of_elements_in_the_list([12, 45, 32, 2, 32, 23, 34, 12, 32, 12]) == 45
