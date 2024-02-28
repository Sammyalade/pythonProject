from account_package.exception import InsufficientFundError


class Account:

    def __init__(self, name: str, pin: str, number: int):
        self.name = name
        self.pin = pin
        self._balance = 0
        self._account_number = 0

    def deposit(self, amount: int):
        self._is_valid_amount(amount)
        self._balance += amount

    def check_balance(self, pin: str):
        self.is_valid_pin(pin)
        return self._balance

    def withdraw(self, amount: int, pin: str):
        if self._is_valid_balance(amount) or self.is_valid_pin(pin):
            return 'Insufficient funds'
        return self._balance - amount

    def is_valid_pin(self, pin) -> bool:
        return self.pin == pin

    def _is_valid_balance(self, amount):
        if self._balance < amount:
            raise InsufficientFundError

    @staticmethod
    def _is_valid_amount(amount):
        if amount < 0:
            raise ValueError("Invalid amount")

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account Name: {self.name} Balance: {self._balance} Account Number: {self._account_number}"
