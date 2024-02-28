class InsufficientFundError(BaseException):

    def __init__(self, message="Invalid Amount"):
        super().__init__(message)

    def __str__(self):
        return f"Insufficient Fund"
