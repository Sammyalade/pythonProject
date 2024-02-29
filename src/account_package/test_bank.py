import pytest

from account_package.bank import BankAccount
from account_package.exception.InvalidAmountError import InvalidAmountError
from account_package.exception.InvalidPinError import InvalidPinError


class TestBank:

    def setup_method(self, method):
        self.bank = BankAccount("Jeremy Bank")
        self.bank.register_account("John Terry", "1122")

    def test_that_account_is_created_when_user_register(self):
        assert self.bank.get_number_of_accounts() == 1

    def test_that_user_can_deposit_after_registration(self):
        self.bank.deposit(1, 1000)
        assert self.bank.check_balance(1, "1122")

    def test_that_user_cannot_deposit_negative_balance(self):
        with pytest.raises(InvalidAmountError):
            self.bank.deposit(1, -12_000)

    def test_that_user_can_withdraw(self):
        self.bank.deposit(1, 10_000)
        self.bank.withdraw(1, 1_000, "1122")
        assert self.bank.check_balance(1, '1122') == 9_000

    def test_that_user_cannot_withdraw_more_than_their_balance(self):
        with pytest.raises(ValueError):
            self.bank.withdraw(1, 1_000, "1122")

    def test_that_user_cannot_withdraw_negative_balance(self):
        with pytest.raises(ValueError):
            self.bank.withdraw(1, -1_000, "1122")

    def test_that_user_cannot_withdraw_with_incorrect_pin(self):
        self.bank.deposit(1, 1000)
        with pytest.raises(InvalidPinError):
            self.bank.withdraw(1, 500, "122")

    def test_that_user_can_transfer_money_to_another_account(self):
        self.bank.register_account("Miriam Emmanuel", "2233")
        self.bank.deposit(1, 10_000)
        self.bank.transfer(1, 2, 5_000, "1122")
        assert self.bank.check_balance(1, '1122') == 5_000
        assert self.bank.check_balance(2, "2233") == 5_000

    def test_that_sender_cannot_transfer_more_than_their_balance(self):
        self.bank.register_account("Miriam Emmanuel", "2233")
        self.bank.deposit(1, 10_000)
        with pytest.raises(ValueError):
            self.bank.transfer(1, 2, 11_000, "1122")

    def test_that_sender_cannot_transfer_negative_balance(self):
        self.bank.register_account("Miriam Emmanuel", "2233")
        with pytest.raises(ValueError):
            self.bank.transfer(1, 2, -11_000, "1122")

    def test_that_user_cannot_transfer_to_non_existing_account(self):
        self.bank.deposit(1, 10_000)
        with pytest.raises(ValueError):
            self.bank.transfer(1, 2, 10_000, "1122")

    def test_that_user_cannot_transfer_with_wrong_pin(self):
        self.bank.register_account("Miriam Emmanuel", "2233")
        self.bank.deposit(1, 10_000)
        with pytest.raises(InvalidPinError):
            self.bank.transfer(1, 2, 11_000, "112")

    def test_that_user_can_close_account(self):
        self.bank.register_account("Miriam Emmanuel", "2233")
        self.bank.remove_account(1, "1122")
        assert self.bank.get_number_of_accounts() == 1

    def test_that_user_cannot_close_account_with_wrong_pin(self):
        self.bank.register_account("Miriam Emmanuel", "2233")
        with pytest.raises(InvalidPinError):
            self.bank.remove_account(1, "122")

    def test_check_balance_with_wrong_pin(self):
        self.bank.deposit(1, 1_000_000)
        with pytest.raises(InvalidPinError):
            self.bank.check_balance(1, "1111")

    def test_deposit_in_account_that_does_not_exist(self):
        with pytest.raises(ValueError):
            self.bank.deposit(100, 12_345)

