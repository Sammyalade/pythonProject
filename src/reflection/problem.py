import type


class Problem:
    name: str
    type: type
    isSolved: bool

    def __init__(self, name: str, type: type):
        self.name = name
        self.type = type
