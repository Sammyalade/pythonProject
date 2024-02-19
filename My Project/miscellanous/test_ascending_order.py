import ascending_order

def test_ascending_order():
    numbers = [1, 2, 3, 2, 5, 7, 1]
    assert ascending_order.sort_list_in_ascending_order(numbers) == '[1, 1, 2, 2, 3, 5, 7]'