from account_package import account_for_bank


class TestAccount:

    def setup_method(self, method):
        self.account: account_for_bank.Account = account_for_bank.Account("Abbey Elliot", "password")

    def test_deposit_3k_balance_is_3k(self):
        self.account.deposit(3_000)
        assert self.account.check_balance("password") == 3_000
