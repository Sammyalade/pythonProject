from account_package import account_for_bank
from account_package.account_for_bank import Account


class BankAccount:

    def __init__(self, name):
        self.name = name
        self._account_list = []

    def generate_account_number(self):
        account_number = len(self._account_list) + 1
        return account_number

    def register_account(self, account_name, pin):
        account = Account(account_name, pin, self.generate_account_number())
        self._account_list.append(account)

    def deposit(self, account_number, amount):
        account = self.__find_account(account_number)
        if account is None:
            raise ValueError(f"Account number not found")
        else:
            account.deposit(amount)

    def __find_account(self, account_number):
        for account in self._account_list:
            if account.get_account_number() == account_number:
                return account
        return None

    def withdraw(self, account_number, amount, pin):
        account = self.__find_account(account_number)
        account.withdraw(amount, pin)

    def get_number_of_accounts(self):
        return len(self._account_list)

    def transfer(self, sender, receiver, amount, pin):
        sender_account = self.__find_account(sender)
        sender_account.withdraw(amount, pin)
        receiver_account = self.__find_account(receiver)
        receiver_account.deposit(amount)

    def remove_account(self, account_number, pin):
        account = self.__find_account(account_number)
        if not account.is_valid_pin(pin):
            Account.raise_invalid_pin_error()
        else:
            self._account_list.remove(account)

    def check_balance(self, account_number, pin):
        account = self.__find_account(account_number)
        return account.check_balance(pin)

    def find_account_by_name(self, account_name):
        for account in self._account_list:
            if account.get_name == account_name:
                return account
        raise RuntimeError("No such account")
