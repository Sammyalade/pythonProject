import tkinter as ak
from tkinter import simpledialog, messagebox
from account_package.bank import BankAccount
from account_package.exception.InsufficientFundError import InsufficientFundError
from account_package.exception.InvalidAmountError import InvalidAmountError
from account_package.exception.InvalidPinError import InvalidPinError


class BankApp:

    def __init__(self):
        self.bank = BankAccount("Trust Bank")

    def main_menu(self):
        root = ak.Tk()
        root.withdraw()

        response = simpledialog.askstring("Bank App", """
           ************************
            Welcome to Trust Bank
            1. Open Account
            2. Deposit Money
            3. Withdraw Money
            4. Transfer Money
            5. Check Balance
            6. Check Account Details
            7. Close Account
            8. Exit App
           ************************
        """)

        if response is not None:
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
        first_name = simpledialog.askstring("Bank App", "Enter your first name: ")
        last_name = simpledialog.askstring("Bank App", "Enter your Last Name: ")
        pin = simpledialog.askstring("Bank App", "Set your pin: ")
        try:
            self.bank.register_account(first_name + " " + last_name, pin)
            messagebox.showinfo("Bank App", f"""
            Account successfully registered.
            {self.bank.register_account(first_name + " " + last_name, pin)}
            """)
        except Exception as e:
            messagebox.showinfo("Error", f"{e.__repr__()}")
        finally:
            self.main_menu()

    def deposit_money(self):
        account_number = simpledialog.askinteger("Bank App", "Enter your account number: ")
        amount = simpledialog.askinteger("Bank App", "Enter the amount to deposit: ")
        self.bank.deposit(account_number, amount)
        try:
            messagebox.showinfo("Bank App", "Deposit success")
        except InvalidAmountError as e:
            messagebox.showinfo(e.__str__())
        except Exception as e:
            messagebox.showinfo("Please try again")
        finally:
            self.main_menu()

    def withdraw_money(self):
        account_number = simpledialog.askinteger("Bank App", "Enter your account number:")
        amount = simpledialog.askinteger("Bank App", "Enter the amount to withdraw:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        try:
            self.bank.withdraw(account_number, amount, pin)
            messagebox.showinfo("Bank App", "Withdraw successful")
        except InvalidAmountError as e:
            messagebox.showerror(e.__str__())
        except InvalidPinError as e:
            messagebox.showinfo(e.__str__())
        except InsufficientFundError as e:
            messagebox.showinfo(e.__str__())
        except Exception as e:
            messagebox.showinfo("Please try again")
        finally:
            self.main_menu()

    def transfer_money(self):
        sender = simpledialog.askinteger("Bank App", "Enter your account number:")
        receiver = simpledialog.askinteger("Bank App", "Enter your receiver account number:")
        amount = simpledialog.askinteger("Bank App", "Enter the amount to transfer:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        try:
            self.bank.transfer(sender, receiver, amount, pin)
            messagebox.showinfo("Bank App", "Transfer successful")
        except InvalidAmountError as e:
            messagebox.showerror(e.__str__())
        except InvalidPinError as e:
            messagebox.showinfo(e.__str__())
        except InsufficientFundError as e:
            messagebox.showinfo(e.__str__())
        except Exception as e:
            messagebox.showinfo("Please try again")
        finally:
            self.main_menu()

    def check_balance(self):
        account_number = simpledialog.askinteger("Bank App", "Enter your account number:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        balance = self.bank.check_balance(account_number, pin)
        try:
            messagebox.showinfo("Bank App", f"Balance is {balance}")
        except InvalidPinError as e:
            messagebox.showinfo(e.__str__())
        except Exception as e:
            messagebox.showinfo("Please try again")
        finally:
            self.main_menu()

    def close_account(self):
        account_number = simpledialog.askinteger("Bank App", "Enter your account number:")
        pin = simpledialog.askstring("Bank App", "Enter your pin:")
        try:
            self.bank.remove_account(account_number, pin)
            messagebox.showinfo("Bank App", "Account closed")
        except InvalidPinError as e:
            messagebox.showinfo(e.__str__())
        except Exception as e:
            messagebox.showinfo("Please try again")
        finally:
            self.main_menu()

    def find_account(self):
        account_name = simpledialog.askstring("BankApp", "Enter your account name(FirstName, space and LastName: ")
        messagebox.showinfo(self.bank.find_account_by_name(account_name))

    def exit_app(self):
        exit(0)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main_menu()
