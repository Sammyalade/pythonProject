class StringDisplay:

    def __init__(self):
        self.message = ""

    def get_string(self, message):
        self.message = message

    def print_string(self):
        return self.message

    def __str__(self):
        return self.message.upper()


if __name__ == "__main__":
    display = StringDisplay()
    display.get_string("Display Message")
    print(display.print_string())
