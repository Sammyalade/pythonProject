class InvalidPinError(BaseException):

    def __init__(self, message="Invalid Amount"):
        super().__init__(message)
