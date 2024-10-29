from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_starting_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_numbers_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AA22A2") == False
    assert is_valid("AAA022") == False
    assert is_valid("CS50") == True

def test_special_characters():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS#50") == False
