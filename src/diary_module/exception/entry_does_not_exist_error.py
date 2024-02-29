class EntryDoesNotExistError(BaseException):
    def __init__(self):
        super().__init__("Entry is empty")