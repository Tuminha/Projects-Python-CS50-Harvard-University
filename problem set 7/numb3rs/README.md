# NUMB3RS - IPv4 Address Validator

## Overview
This program validates IPv4 addresses, inspired by the TV show NUMB3RS where an invalid IP address (275.3.6.28) appeared on screen. The program ensures that each octet in an IPv4 address is within the valid range of 0-255.

## Problem Context
In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen: **275.3.6.28**. This isn't actually a valid IPv4 address because 275 exceeds the maximum value of 255 for any octet.

## Requirements
Implement a function called `validate` that:
- Takes an IPv4 address as input (string)
- Returns `True` if the address is valid
- Returns `False` if the address is invalid

## IPv4 Address Rules
An IPv4 address must:
- Be formatted as #.#.#.# (four octets separated by dots)
- Each octet must be a number between 0 and 255 (inclusive)
- Leading zeros are considered invalid (e.g., 192.168.001.1 is invalid)
- Must contain exactly four octets

## Implementation Details

### Regex Pattern Breakdown
The validation uses a sophisticated regex pattern that ensures each octet is valid:

```python
r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)\.'
```

**Pattern explanation:**
- `25[0-5]` - Matches 250-255
- `2[0-4]\d` - Matches 200-249  
- `1\d\d` - Matches 100-199
- `[1-9]\d?` - Matches 10-99 (no leading zeros)
- `0` - Matches single 0 (no leading zeros)

### Key Features
- **No external libraries** - Only uses `re` and `sys` as allowed
- **Leading zero prevention** - Regex pattern excludes numbers like 001, 01
- **Range validation** - Ensures each octet is 0-255
- **Format validation** - Ensures proper IPv4 structure

## Usage Examples

### Valid IPv4 Addresses
```bash
127.0.0.1        # Localhost
255.255.255.255  # Broadcast address
192.168.1.1      # Private network
10.0.0.1         # Private network
172.16.0.1       # Private network
```

### Invalid IPv4 Addresses
```bash
512.512.512.512  # Octets > 255
1.2.3.1000       # Octet > 255
192.168.001.1    # Leading zeros
275.3.6.28       # Octet > 255 (from NUMB3RS)
cat               # Non-numeric input
1.2.3            # Too few octets
1.2.3.4.5        # Too many octets
```

## Testing

### Manual Testing
Run the program and test various inputs:
```bash
python3 numb3rs.py
# Then enter test addresses when prompted
```

### Automated Testing
The `test_numb3rs.py` file contains comprehensive tests:
```bash
pytest test_numb3rs.py
```

**Test Cases Covered:**
- ✅ Valid addresses: `127.0.0.1`, `255.255.255.255`
- ❌ Invalid addresses: `512.512.512.512`, `1.2.3.1000`
- ❌ Leading zeros: `192.168.001.1`
- ❌ Non-numeric: `cat`

## CS50 Check50 Results
✅ All tests passed successfully!

## Files
- `numb3rs.py` - Main program with IPv4 validation function
- `test_numb3rs.py` - Comprehensive test suite using pytest
- `README.md` - This documentation file

## Submission
This exercise is ready for submission to CS50 using:
```bash
submit50 cs50/problems/2022/python/numb3rs
```

## Learning Outcomes
- **Regular Expressions**: Advanced regex pattern creation and usage
- **IPv4 Protocol**: Understanding of IP address structure and validation rules
- **Input Validation**: Robust error checking and edge case handling
- **Testing**: Comprehensive test coverage with pytest
- **Problem Solving**: Breaking down complex validation into regex patterns

## Technical Notes
- Uses `re.compile()` for efficient pattern matching
- `bool(pattern.match(ip))` returns True/False based on match
- Pattern ensures no leading zeros while allowing single 0
- Handles edge cases like maximum values (255) correctly

## Fun Fact
The exercise name comes from the TV show NUMB3RS, which featured mathematical problem-solving. The invalid IP address 275.3.6.28 in the show would have been caught by this validator!
