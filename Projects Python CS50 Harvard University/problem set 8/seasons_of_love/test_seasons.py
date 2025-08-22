# test the seasons.py file

import pytest
from datetime import date
from seasons import main
import sys
from io import StringIO

def test_one_year_ago():
    # Test with a date one year ago
    one_year_ago = date.today().replace(year=date.today().year - 1)
    birth_date_str = one_year_ago.isoformat()
    
    # Mock input and capture output
    import unittest.mock
    with unittest.mock.patch('builtins.input', return_value=birth_date_str):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # Check if output contains the expected words for minutes (five hundred twenty-five thousand, six hundred)
            assert "five hundred twenty-five thousand, six hundred" in output.lower()

def test_two_years_ago():
    # Test with a date two years ago
    two_years_ago = date.today().replace(year=date.today().year - 2)
    birth_date_str = two_years_ago.isoformat()
    
    # Mock input and capture output
    import unittest.mock
    with unittest.mock.patch('builtins.input', return_value=birth_date_str):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # Check if output contains the expected words for minutes (one million, fifty thousand range)
            assert "one million" in output.lower() and "thousand" in output.lower()

def test_invalid_format():
    # Test with invalid date format
    invalid_date = "invalid-date"
    
    # Mock input and test that sys.exit is called
    import unittest.mock
    with unittest.mock.patch('builtins.input', return_value=invalid_date):
        with pytest.raises(SystemExit):
            main()

def test_empty_input():
    # Test with empty input
    import unittest.mock
    with unittest.mock.patch('builtins.input', return_value=""):
        with pytest.raises(SystemExit):
            main()