from account import Account
import pytest


class TestAccount:

    def setup_method(self, method):
        self.account: Account = Account("Abbey Elliot", "password")

    def test_deposit_3k_balance_is_3k(self):
        self.account.deposit(3_000)
        assert self.account.check_balance("password") == 3_000
