import pytest
from working import convert


def test_correct():
    """Test correct time conversions"""
    # Basic conversions
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    
    # Edge cases with 12
    assert convert("12:00 AM") == "00:00"
    assert convert("12:00 PM") == "12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    
    # Other times
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_incorrect():
    """Test that invalid inputs raise ValueError"""
    # Invalid minutes (60+)
    with pytest.raises(ValueError):
        convert("9:60 AM")
    
    # Invalid hours (0 or 13+)  
    with pytest.raises(ValueError):
        convert("13:00 PM")
    
    # Wrong format
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    
    # Missing "to"
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")