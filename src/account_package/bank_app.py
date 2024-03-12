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
        6. Check Acount Details
        7. Close Account
        8. Exit App
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
                self.find_account()
            case '7':
                self.close_account()
            case '8':
                self.exit_app()

    def open_account(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your Last Name: ")
        pin = input("Set your pin: ")
        self.bank.register_account(first_name + " " + last_name, pin)
        print(f"Account successfully registered")

        self.main_menu()

    def deposit_money(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter the amount to deposit"))
        self.bank.deposit(account_number, amount)
        print(f"Deposit success")
        self.main_menu()

    def withdraw_money(self):
        account_number = int(input("Enter your account number: "))
        amount = input("Enter the amount to withdraw")
        pin = input("Enter your pin: ")
        self.bank.withdraw(account_number, amount, pin)
        print(f"Withdraw successful")
        self.main_menu()

    def transfer_money(self):
        sender = int(input("Enter your account number: "))
        receiver = int(input("Enter your receiver account number: "))
        amount = input("Enter the amount to transfer")
        pin = input("Enter your pin: ")
        self.bank.transfer(sender, receiver, amount, pin)
        print(f"Transfer successful")
        self.main_menu()

    def check_balance(self):
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your pin: ")
        print(f"Balance is {self.bank.check_balance(account_number, pin)}")
        self.main_menu()

    def close_account(self):
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your pin: ")
        self.bank.remove_account(account_number, pin)
        self.main_menu()

    def exit_app(self):
        exit(0)

    def find_account(self):
        account_name = input("Enter your account name(FirstName, space and LastName: ")
        print(self.bank.check_account_details(account_name))


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main_menu()
