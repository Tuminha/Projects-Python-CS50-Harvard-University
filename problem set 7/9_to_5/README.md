# 9 to 5

## Problem Description

Write a program that converts 12-hour time format to 24-hour time format. The program should handle both single times and time ranges.

## Requirements

- Accept input in 12-hour format (e.g., "9:00 AM", "5:30 PM")
- Handle time ranges with " to " separator (e.g., "9 AM to 5 PM")
- Convert to 24-hour format (e.g., "09:00 to 17:00")
- Raise ValueError for invalid inputs
- Only import `sys` and `re` libraries

## Input Format

The program accepts:
- Single times: "9:00 AM", "5:30 PM", "12:00 AM"
- Time ranges: "9 AM to 5 PM", "10:30 PM to 8:00 AM"
- Hours: 1-12
- Minutes: 00-59
- AM/PM indicators

## Output Format

- Single times: "09:00", "17:30", "00:00"
- Time ranges: "09:00 to 17:00", "22:30 to 08:00"

## Examples

| Input | Output |
|-------|--------|
| "9 AM to 5 PM" | "09:00 to 17:00" |
| "9:00 AM to 5:00 PM" | "09:00 to 17:00" |
| "12:00 AM to 12:00 PM" | "00:00 to 12:00" |
| "10:30 PM to 8 AM" | "22:30 to 08:00" |
| "9:00 AM" | "09:00" |
| "5:30 PM" | "17:30" |

## Error Cases

The program raises ValueError for:
- Invalid hours (0, 13+)
- Invalid minutes (60+)
- Wrong separators (e.g., "9 AM - 5 PM")
- Missing "to" in ranges
- Invalid formats

## Implementation Details

- Uses regex to parse time formats
- Validates hours (1-12) and minutes (0-59)
- Handles edge cases like 12 AM (→ 00:00) and 12 PM (→ 12:00)
- Converts PM times by adding 12 (except 12 PM)
- Formats output with zero-padding

## Files

- `working.py` - Main implementation
- `test_working.py` - Test suite using pytest
- `README.md` - This documentation

## Testing

Run the test suite:
```bash
python -m pytest test_working.py -v
```

## CS50 Checker

Verify with CS50's checker:
```bash
python -m check50 cs50/problems/2022/python/working
```
