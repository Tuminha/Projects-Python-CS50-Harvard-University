#mplement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_bank.py
import pytest
from bank import value

def test_hello_greetings():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello, newman") == 0
    assert value("Hello there!") == 0

def test_h_greetings():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("how are you?") == 20
    assert value("Hi there!") == 20

def test_other_greetings():
    assert value("what's up?") == 100
    assert value("good morning") == 100
    assert value("GOOD MORNING") == 100
    assert value("sup") == 100

def test_case_sensitivity():
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("HeLLo") == 0
    assert value("Hi") == 20
    assert value("HI") == 20