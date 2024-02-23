from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0.00:
            raise ValueError("Invalid Balance for balance")
        self.__balance = balance

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"


ai = Account("Dayone", Decimal(10))

print(ai)
