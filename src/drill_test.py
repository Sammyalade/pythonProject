import drill


class TestDrill:
    def test_function_can_take_and_print_a_message(self):
        self.string_print = drill.StringDisplay()
        self.string_print.get_string("Hello World")
        assert self.string_print.print_string() == "Hello World"

    def test_that_string_can_print_uppercase(self):
        self.string_print = drill.StringDisplay()
        self.string_print.get_string("Hello World")
        assert self.string_print.__str__() == "HELLO WORLD"
