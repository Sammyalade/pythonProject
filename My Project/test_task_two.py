import task_two


def test_collect_ten_input_without_saving_duplicate():
    assert task_two.collect_ten_input_without_saving_duplicate([1, 4, 2, 5, 6, 2, 3, 3, 1, 6, 9, 7]) == [1, 4, 2, 5, 6,
                                                                                                         3, 9, 7]


def test_sum_collection():
    assert task_two.sum_collection({1, 3, 4, 6, 8, 9}) == 31


def test_remove_item():
    assert task_two.remove_item({1, 3, 4, 6, 8, 9}, 9) == {1, 3, 4, 6, 8}
    assert task_two.remove_item({1, 3, 4, 6, 8, 9}, 15) is None


def test_find_intersection():
    assert task_two.find_intersection({1, 3, 4, 6, 8, 9}, {1, 10, 16, 4, 6, 30}) == {1, 4, 6}
    assert task_two.find_intersection({1, 3, 4, 6, 8, 9}, {10, 16, 30}) is None
