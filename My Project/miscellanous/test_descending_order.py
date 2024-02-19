import descending_order

def test_descending_order():
    numbers = [1, 2, 3, 2, 5, 7, 1]
    assert descending_order.sort_list_in_descending_order(numbers) == '[7, 5, 3, 2, 2, 1, 1]'