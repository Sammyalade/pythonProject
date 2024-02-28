import tkinter as ak
from tkinter import simpledialog, messagebox
from account_package.bank import BankAccount


class BankApp:

    def __init__(self):
        self.bank = BankAccount("Trust Bank")

    def main_menu(self):
        root = ak.Tk()
        root.withdraw()

        response = simpledialog.askstring("Bank App", """
            Welcome to Trust Bank
            1. Open Account
            2. Deposit Money
            3. Withdraw Money
            4. Transfer Money
            5. Check Balance
            6. Close Account
            7. Exit App
        """)

        if response is not None:
            self.match_case(response)

        root.destroy()

    def match_case(self, response):
        if response == '1':
            self.open_account()
        elif response == '2':
            self.deposit_money()
        elif response == '3':
            self.withdraw_money()
        elif response == '4':
            self.transfer_money()
        elif response == '5':
            self.check_balance()
        elif response == '6':
            self.close_account()
        elif response == '7':
            self.exit_app()

    def open_account(self):
        first_name = simpledialog.askstring("Bank App", "Enter your first name:")
        last_name = simpledialog.askstring("Bank App", "Enter your Last Name:")
        pin = simpledialog.askstring("Bank App", "Set your pin:")
        try:
            self.bank.register_account(first_name + " " + last_name, pin)
            messagebox.showinfo("Bank App", "Account successfully registered")
        except BaseException as e:
            messagebox.showerror(e.)
        self.main_menu()

    def deposit_money(self):
        account_number = simpledialog.askstring("Bank App", "Enter your account number:")
        amount = simpledialog.askstring("Bank App", "Enter the amount to deposit:")
        self.bank.deposit(account_number, amount)
        messagebox.showinfo("Bank App", "Deposit success")
        self.main_menu()

    def withdraw_money(self):
        account_number = simpledialog.askstring("Bank App", "Enter your account number:")
        amount = simpledialog.askstring("Bank App", "Enter the amount to withdraw:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        self.bank.withdraw(account_number, amount, pin)
        messagebox.showinfo("Bank App", "Withdraw successful")
        self.main_menu()

    def transfer_money(self):
        sender = simpledialog.askstring("Bank App", "Enter your account number:")
        receiver = simpledialog.askstring("Bank App", "Enter your receiver account number:")
        amount = simpledialog.askstring("Bank App", "Enter the amount to transfer:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        self.bank.transfer(sender, receiver, amount, pin)
        messagebox.showinfo("Bank App", "Transfer successful")
        self.main_menu()

    def check_balance(self):
        account_number = simpledialog.askstring("Bank App", "Enter your account number:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        balance = self.bank.check_balance(account_number, pin)
        messagebox.showinfo("Bank App", f"Balance is {balance}")
        self.main_menu()

    def close_account(self):
        account_number = simpledialog.askstring("Bank App", "Enter your account number:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        self.bank.remove_account(account_number, pin)
        messagebox.showinfo("Bank App", "Account closed")
        self.main_menu()

    def exit_app(self):
        exit(0)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main_menu()
