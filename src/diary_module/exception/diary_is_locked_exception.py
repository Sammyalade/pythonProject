class DiaryIsLockedError(BaseException):
    def __init__(self):
        super().__init__("Diary is locked")
