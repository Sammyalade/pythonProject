from exception import InvalidAmountError, InvalidPinError, InsufficientFundError


class Account:

    def __init__(self, name: str, pin: str, number: int):
        self.name = name
        self.pin = pin
        self._balance = 0
        self._account_number = None

    def deposit(self, amount: int):
        self._balance += amount

    def check_balance(self, pin: str):
        self._is_valid_pin(pin)
        return self._balance

    def withdraw(self, amount: int, pin: str):
        self._is_valid_pin(pin)
        self._is_valid_balance(amount)
        return self._balance - amount

    def is_valid_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinError("Invalid pin")

    def _is_valid_balance(self, amount):
        if self._balance < amount:
            raise InsufficientFundError("Insufficient funds")

    def _is_valid_amount(self, amount):
        if amount < 0:
            raise InvalidAmountError("Invalid amount")

    def get_account_number(self):
        return self.account_number

    def __str__(self):
        return f"Account Name: {self.name} Balance: {self._balance} Account Number: {self.account_number}"
