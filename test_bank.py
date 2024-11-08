import pytest
from bank import Account

def test_initial_balance():
    # TODO
	_init_(self, "DS", balance=0)
    self.get_balance()

def test_deposit():
    # TODO
	_init_(self, "DS", balance=0)
    self.deposit(100.0)

def test_withdraw():
    # TODO
    _init_(self, "DS", balance=0)
	withdraw(10.0)

def test_deposit_negative_amount():
    # TODO
    _init_(self, "DS", balance=0)
	self.deposit(-abs(10))

def test_withdraw_more_than_balance():
    # TODO
    _init_(self, "DS", balance=0)
	self.withdraw(self.get_balance(self) + 100.0)

def test_withdraw_negative_amount():
    # TODO
    _init_(self, "DS", balance=0)
	self.withdraw(-abs(10))
