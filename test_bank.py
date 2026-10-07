# test_bank.py
import pytest
from bank import BankAccount, InsufficientFunds

@pytest.fixture
def account():
    return BankAccount("alice", balance=100)

def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
        assert account.balance == 100

def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100

def test_deposit_of_zero(account):
    with pytest.raises(ValueError, match="must be positive"):
            account.deposit(0)

def test_withdraw_balance_leaves_zero(account):
     account.withdraw(100)
     assert account.balance == 0

def test_two_withdrawal_in_a_row(account):
     account.withdraw(30)
     account.withdraw(50)
     assert account.balance == 20

def test_interest(account):
     account.add_interest(0.10)
     assert account.balance == pytest.approx(110)
