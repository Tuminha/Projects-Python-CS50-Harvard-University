# Response Validation

## Problem Description

Write a program that validates email addresses using the `validators` library. The program prompts the user for an email address and returns whether it's valid or invalid.

## Requirements

- Accept email address input from the user
- Use the `validators` library to check email validity
- Return "Valid" for valid email addresses
- Return "Invalid" for invalid email addresses
- Handle input gracefully

## Input Format

The program accepts any string input from the user, which is then validated as an email address.

## Output Format

- **Valid emails**: Returns "Valid"
- **Invalid emails**: Returns "Invalid"

## Examples

| Input | Output |
|-------|--------|
| `user@example.com` | "Valid" |
| `cisco@periospot.com` | "Valid" |
| `invalid-email` | "Invalid" |
| `@domain.com` | "Invalid" |
| `user@` | "Invalid" |
| `user.domain.com` | "Invalid" |

## Implementation Details

- Uses the `validators` library for robust email validation
- The `validators.email()` function handles all validation logic
- Returns boolean `True`/`False` which is converted to "Valid"/"Invalid"
- No complex regex needed - the library handles edge cases

## Dependencies

- `validators` library (installed via pip)

## Installation

Install the required library in your virtual environment:
```bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org validators
```

## Files

- `response.py` - Main implementation
- `README.md` - This documentation

## Usage

1. Activate your virtual environment:
```bash
source ../../cs50_venv/bin/activate
```

2. Run the program:
```bash
python response.py
```

3. Enter an email address when prompted

## How It Works

1. **Input**: Program prompts for an email address
2. **Validation**: Uses `validators.email()` to check validity
3. **Output**: Returns "Valid" or "Invalid" based on the result

## Email Validation Rules

The `validators` library checks for:
- Proper email format (user@domain.tld)
- Valid domain structure
- Appropriate top-level domains
- RFC compliance

## Error Handling

- No exceptions are raised - invalid emails simply return "Invalid"
- The program handles any input gracefully
- Input validation is handled by the `validators` library

## Testing

Test with various email formats:
- Standard emails: `user@example.com`
- Subdomains: `user@sub.example.com`
- Special characters: `user.name+tag@example.com`
- Invalid formats: `not-an-email`, `@domain.com`, `user@`
