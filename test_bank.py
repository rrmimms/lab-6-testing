import pytest
from bank import Account

def test_initial_balance():
    # TODO
    self = Account("DS")
    self.balance = 100
    self.get_balance() = 100

def test_deposit():
    # TODO
    self = Account("DS")
    self.balance = 0
    self.deposit(100.0) = 100.0

def test_withdraw():
    # TODO
	self = Account("DS")
    self.balance = 100
    withdraw(10.0) = 90.0

def test_deposit_negative_amount():
    # TODO
	self = Account("DS")
    self.balance = 10.0
    self.deposit(-abs(10))

def test_withdraw_more_than_balance():
    # TODO
	self = Account("DS")
    self.balance = 10.0
    self.withdraw(self.get_balance(self) + 100.0)

def test_withdraw_negative_amount():
    # TODO
	self = Account("DS")
    self.balance = 10.0
    self.withdraw(-abs(10))
