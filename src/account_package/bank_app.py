from account_package.bank import BankAccount


class BankApp:

    def __init__(self):
        self.bank = BankAccount("Trust Bank")

    def main_menu(self):
        response = input("""
        1. Open Account
        2. Deposit Money
        3. Withdraw Money
        4. Transfer Money
        5. Check Balance
        6. Close Account
        7. Exit App
        """)
        self.match_case(response)

    def match_case(self, response):
        match response:
            case '1':
                self.open_account()
            case '2':
                self.deposit_money()
            case '3':
                self.withdraw_money()
            case '4':
                self.transfer_money()
            case '5':
                self.check_balance()
            case '6':
                self.close_account()
            case '7':
                self.exit_app()

    def open_account(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your Last Name: ")
        pin = input("Set your pin: ")
        self.bank.register_account(first_name + " " + last_name, pin)
        return f"Account successfully registered"

    def deposit_money(self):
        account_number = input("Enter your account number: ")
        amount = input("Enter the amount to deposit")
        self.bank.deposit(account_number, amount)
        return f"Deposit success"

    def withdraw_money(self):
        account_number = input("Enter your account number: ")
        amount = input("Enter the amount to withdraw")
        pin = input("Enter your pin: ")
        self.bank.withdraw(account_number, amount, pin)
        return f"Withdraw successful"

    def transfer_money(self):
        sender = input("Enter your account number: ")
        receiver = input("Enter your receiver account number: ")
        amount = input("Enter the amount to transfer")
        pin = input("Enter your pin: ")
        self.bank.transfer(sender, receiver, amount, pin)
        return f"Transfer successful"

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        return f"Balance is {self.bank.check_balance(account_number, pin)}"

    def close_account(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        self.bank.remove_account(account_number, pin)

    def exit_app(self):
        exit(0)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main_menu()