from account_for_bank import Account


class BankAccount:

    def __init__(self, name):
        self.name = name
        self._account_list = []
        self.account_number_generator = 0

    def register_account(self, account_name, pin):
        self._account_list.append(Account(account_name, pin, self.account_number_generator + 1))

    def deposit(self, account_number, amount):
        for account in self._account_list:
            if account_number == account.get_account_number():
                account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        for account in self._account_list:
            if account_number == account.get_account_number():
                account.withdraw(amount, pin)

    def get_number_of_accounts(self):
        return len(self._account_list)

    def transfer(self, sender, receiver, amount, pin):
        for account in self._account_list:
            if account.get_account_number() == sender:
                account.withdraw(amount, pin)
        for account in self._account_list:
            if account.get_account_number() == receiver:
                account.deposit(amount)

    def remove_account(self, account_number, pin):
        for account in self._account_list:
            if account.get_account_number() == account_number:
                account.is_valid_pin(pin)
                if account.get_account_number() == account_number:
                    self._account_list.remove(account)

    def check_balance(self, account_number, pin):
        for account in self._account_list:
            if account.get_account_number() == account_number:
                return f"{account.check_balance(pin)}"




