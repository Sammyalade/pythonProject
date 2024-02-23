from account import Account


class BankAccount:

    def __init__(self, name):
        self.name = name
        self._account_list = []
        self.account_number_generator = 0

    def register_account(self):
        account_name = input("Enter your Full name: ")
        pin = input("Enter your PIN: ")
        self._account_list.append(Account(account_name, pin, self.account_number_generator + 1))

    def deposit(self, account_number, amount):
        for account in self._account_list:
            if account_number == account.get_account_number():
                account.deposit(amount)
