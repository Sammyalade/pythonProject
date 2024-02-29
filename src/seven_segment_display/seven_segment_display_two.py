class SevenSegmentDisplayTwo:

    def __init__(self, switch):
        self.switch = switch
        self.my_dict = {}
        self.count = 0
        self.display = [["*  *  *  *"], ["*"], ["*"], ["*"]]

    def initialize_dictionary(self):
        for letter, char in zip("abcdefgh", self.switch):
            self.count += 1
            check_number = int(char)
            if check_number > 1 or check_number < 0:
                raise ValueError(f"Character at {self.count} is invalid")
            self.my_dict[letter] = check_number
        print(self.my_dict)

    def control_print(self):
        for i in self.my_dict:
            if self.my_dict['h'] == 1:
                if self.my_dict['a'] == 1:
                    print(self.display[0][0])


if __name__ == '__main__':
    segment = SevenSegmentDisplayTwo("01100101")
    segment.initialize_dictionary()
    #segment.control_printing()

