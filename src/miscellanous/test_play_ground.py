from unittest import TestCase
import play_ground


class Test(TestCase):
    def test_get_length(self):
        sample_list = list(range(10, 20))
        assert 10 == play_ground.get_length(sample_list)
        assert 25 == play_ground.get_length(list(range(1, 26)))

    def test_that_function_can_sum_of_element_in_even_position(self):
        assert 25 == play_ground.sum_of_element_in_even_position(list(range(1, 11)))

    def test_that_function_can_sum_of_element_in_odd_position(self):
        assert 30 == play_ground.sum_of_element_in_odd_position(list(range(1, 11)))


    def test_that_function_can_multiply_elements_at_third_positions():
        assert 162 == play_ground.multiply_elements_at_third_positions(list(range(1, 11)))