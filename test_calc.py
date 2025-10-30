import pytest

from calc import add, sub, mul, div

def test_add():
    # compare actual o/p and expected o/p
    assert add(2,3) ==  5
    # assert will check actual o/p to expected o/p if both are same then will pass test

def test_sub():
    assert sub(3,1) == 2

def test_mul():
    assert mul(3,2) == 6

def test_div():
    assert div(4,2) == 2 