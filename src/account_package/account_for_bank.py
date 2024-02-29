from account_package.exception import InsufficientFundError
from account_package.exception.InvalidAmountError import InvalidAmountError
from account_package.exception.InvalidPinError import InvalidPinError


class Account:

    def __init__(self, name: str, pin: str, number: int):
        self.name = name
        self.pin = pin
        self._balance = 0
        self._account_number = number

    def deposit(self, amount: int):
        if not self._is_valid_amount(amount):
            raise InvalidAmountError("Invalid amount")
        else:
            self._balance += amount

    def check_balance(self, pin: str):
        if not self.is_valid_pin(pin):
            self.raise_invalid_pin_error()
        return self._balance

    @staticmethod
    def raise_invalid_pin_error():
        raise InvalidPinError

    def withdraw(self, amount: int, pin: str):
        if not self.is_valid_pin(pin):
            self.raise_invalid_pin_error()
        elif not self._is_valid_balance(amount):
            raise ValueError("Insufficient balance")
        elif amount < 0:
            raise ValueError("Negative amount")
        else:
            self._balance -= amount

    def is_valid_pin(self, pin):
        return self.pin == pin

    def _is_valid_balance(self, amount):
        return self._balance > amount

    @staticmethod
    def _is_valid_amount(amount: int):
        return amount > 0

    def get_account_number(self):
        return self._account_number

    def __repr__(self):
        return f"Account Name: {self.name} Balance: {self._balance} Account Number: {self._account_number}"
