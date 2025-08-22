# We have to test '127.0.0.1' and return True
# We have to test '255.255.255.255' and return True
# We have to test '512.512.512.512' and return False
# We have to test '1.2.3.1000' and return False
# We have to test '192.168.001.1' and return False
# We have to test 'cat' and return False

import pytest
from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False

if __name__ == "__main__":
    pytest.main()

# Run the tests with pytest test_numb3rs.py