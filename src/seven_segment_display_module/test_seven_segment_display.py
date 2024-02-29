import pytest

from seven_segment_display_module import seven_segment_display


class TestSevenSegmentDisplay:

    def test_that_when_you_put_a_list_more_than_8_exception_is_thrown(self):
        obj = seven_segment_display.SevenSegmentDisplay("10001010111")
        with pytest.raises(RuntimeError):
            obj.put_in_a_list()

    def test_that_when_you_put_less_than_8_exception_is_thrown(self):
        obj = seven_segment_display.SevenSegmentDisplay("1000")
        with pytest.raises(RuntimeError):
            obj.put_in_a_list()

    def test_when_you_put_any_number_aside_zero_and_one_exception_is_thrown(self):
        obj = seven_segment_display.SevenSegmentDisplay("10001122")
        with pytest.raises(ValueError):
            obj.put_in_a_list()

    def test_horizontal_print(self):
        obj = seven_segment_display.SevenSegmentDisplay("11010101")
        assert obj.print_horizontal() == "*  *  *  *"


