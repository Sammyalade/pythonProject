import number_checker

def test_number_checker():
    numbers = [1, 2, 3, 2, 5, 7, 1]
    assert number_checker.check_for_a_number(numbers, 7) == '5'