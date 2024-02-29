import pytest

from seven_segment_display_module import seven_segment_display


class TestSevenSegmentDisplay:

    def test_that_when_you_put_a_list_more_than_8_exception_is_thrown(self):
        obj = seven_segment_display.SevenSegmentDisplay("10001010111")
        with pytest.raises(RuntimeError):
            obj.put_in_a_list()

