import pytest

from account_package import account_for_bank


class TestAccount:

    def setup_method(self, method):
        self.account: account_for_bank.Account = account_for_bank.Account("Abbey Elliot", "password", 1)

    def test_deposit_3k_balance_is_3k(self):
        self.account.deposit(3_000)
        assert self.account.check_balance("password") == 3_000

    def test_deposit_minus3k_throws_InvalidAmountError(self):
        with pytest.raises(ValueError):
            self.account.deposit(-3_000)

    def test_deposit_2k_withdraw_1k_with_valid_pin(self):
        self.account.deposit(2_000)
        self.account.withdraw(1_000, "password")
        assert self.account.check_balance("password") == 1_000
