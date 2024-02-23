from exception import InvalidPinError
from exception import InsufficientFundError


class Account:

    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin = pin
        self._balance = 0
        self.account_number = None

    def deposit(self, amount: int):
        self._balance += amount

    def check_balance(self, pin: str):
        self._is_valid_pin(pin)
        return self._balance

    def withdraw(self, amount: int, pin: str):
        self._is_valid_pin(pin)
        self._is_valid_balance(amount)
        return self._balance - amount

    def _is_valid_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinError("Invalid pin")

    def _is_valid_balance(self, amount):
        if self._balance < amount:
            raise InsufficientFundError("Insufficient funds")

    def __str__(self):
        return f"Account Name: {self.name} Balance: {self._balance} Account Number: {self.account_number}"
