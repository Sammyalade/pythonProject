import task_one


def test_add_every_third_element():
    list1 = list(range(1, 16))
    assert task_one.add_every_third_element(list1) == 45


def test_calculate_sum_of_last_middle_and_last_element():
    list1 = list(range(1, 16))
    assert task_one.calculate_sum_of_last_middle_and_last_element(list1) == 23.5
