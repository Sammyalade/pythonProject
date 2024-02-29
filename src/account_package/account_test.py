import pytest

from account_package.account_for_bank import Account
from account_package.exception.InvalidAmountError import InvalidAmountError
from account_package.exception.InvalidPinError import InvalidPinError


class TestAccount:

    def test_deposit(self):
        account = Account("John", "1234", 1)
        account.deposit(2_000)
        assert account.check_balance("1234") == 2_000

    def test_deposit_negative_amount_InvalidAmountErrorIsThrown(self):
        account = Account("John", "1234", 1)
        with pytest.raises(InvalidAmountError):
            account.deposit(-1_000)

    def test_withdraw(self):
        account = Account("John", "1234", 1)
        account.deposit(3_000)
        account.withdraw(2_000, "1234")
        assert account.check_balance("1234") == 1_000

    def test_withdraw_when_balance_is_zero_throwsInsufficientFundError(self):
        account = Account("John", "1234", 1)
        with pytest.raises(ValueError):
            account.withdraw(1_000, "1234")

    def test_withdraw_when_pin_is_wrong_raisesInvalidPinError(self):
        account = Account("John", "1234", 1)
        account.deposit(100_000)
        with pytest.raises(InvalidPinError):
            account.withdraw(50_000, "1233")

    def test_withdraw_negative_amount_throwsInvalidAmountError(self):
        account = Account("John", "1234", 1)
        with pytest.raises(ValueError):
            account.withdraw(-1_000, "1234")

    def test_check_balance_when_pin_is_wrong_raisesInvalidPinError(self):
        account = Account("John", "1234", 1)
        account.deposit(1_000)
        with pytest.raises(InvalidPinError):
            account.check_balance("1122")

    def test_account_display(self):
        account = Account("John", "1234", 1)
        assert account.__repr__() == "Account Name: John Balance: 0 Account Number: 1"

    def test_that_get_account_number__returns_correct_account_number(self):
        account = Account("John", "1234", 1)
        assert account.get_account_number() == 1
