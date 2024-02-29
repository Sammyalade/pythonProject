class SevenSegmentDisplayTwo:

    def __init__(self, number_segment: str):
        self.count = 0
        self.number_segment = number_segment
        self.segments = {}

    def print_horizontal(self):
        return f"*  *  *  *"

    @staticmethod
    def print_vertical_left():
        vertical_left1 = "*"
        vertical_left2 = "*"
        vertical_left3 = "*"
        return f"{vertical_left1}\n{vertical_left2}\n{vertical_left3}\n"

    @staticmethod
    def print_vertical_right():
        vertical_right1 = "         *"
        vertical_right2 = "         *"
        vertical_right3 = "         *"
        return f"{vertical_right1}\n{vertical_right2}\n{vertical_right3}\n"

    @staticmethod
    def print_vertical_right_and_left():
        vertical_right_and_left1 = "*        *"
        vertical_right_and_left2 = "*        *"
        vertical_right_and_left3 = "*        *"
        return f"{vertical_right_and_left1}\n{vertical_right_and_left2}\n{vertical_right_and_left3}\n"

    def put_in_a_list(self):
        my_list = []
        my_list += self.number_segment
        for number in my_list:
            self.count += 1
            if number not in ['0', '1']:
                raise ValueError(f"Character at {self.count} is invalid")
        if len(my_list) > 8 or len(my_list) < 8:
            raise RuntimeError("Input should not be more than or less than 7 numbers")
        return my_list

    def print(self):
        list1 = self.put_in_a_list()
        if list1[7] == '1':
            print(self.control_horizontal_printing(list1[0]))
            print(self.control_vertical_printing(list1[1], list1[5]))
            print(self.control_horizontal_printing(list1[6]))
            print(self.control_vertical_printing(list1[2], list1[4]))
            print(self.control_horizontal_printing(list1[3]))

    def control_horizontal_printing(self, switch: str):
        if switch == '1':
            self.print_horizontal()

    def control_vertical_printing(self, switch1, switch2):
        if switch1 == '1' and switch2 == '1':
            self.print_vertical_right_and_left()
        elif switch2 == '1' and switch1 == '0':
            self.print_vertical_left()
        elif switch2 == '0' and switch1 == '1':
            self.print_vertical_right()


if __name__ == '__main__':
    segment = SevenSegmentDisplayTwo("11110111")
    segment.print()
