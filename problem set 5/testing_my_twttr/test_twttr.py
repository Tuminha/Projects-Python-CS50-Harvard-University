#implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_twttr.py
import pytest
from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("Hi") == "H"
    assert shorten("CS50") == "CS50"