# 🎭 Seasons of Love

## 📖 Project Overview

**Seasons of Love** is a Python program that calculates how old someone is in minutes and displays the result in English words, inspired by the iconic song from the musical *Rent*. The program prompts users for their birthdate and converts the time difference into a poetic, word-based representation of minutes.

> *"Five hundred twenty-five thousand, six hundred minutes... How do you measure, measure a year?"*

## 🎯 Learning Objectives

This project focuses on:
- **Object-Oriented Programming** concepts
- Working with the **datetime** module
- **Date calculations** and time arithmetic
- **Input validation** and error handling
- **String formatting** and number-to-word conversion
- **Unit testing** with pytest
- **Program structure** with main functions and modular design

## 🚀 Features

### Core Functionality
- **Birthdate Input**: Accepts dates in YYYY-MM-DD format
- **Age Calculation**: Computes exact age in minutes from birth to current date
- **Word Conversion**: Displays minutes in English words (e.g., "Five hundred twenty-five thousand, six hundred minutes")
- **Leap Year Handling**: Automatically accounts for leap years in calculations
- **Error Handling**: Gracefully exits with `sys.exit()` for invalid date formats

### Technical Features
- **Modular Design**: Separated into logical functions for maintainability
- **Comprehensive Testing**: Full test suite with pytest
- **Input Validation**: Robust date format checking
- **Exception Safety**: No exceptions raised during normal operation

## 🛠️ Implementation Details

### Program Structure
```python
from datetime import date

def main():
    # Main program logic
    
def get_birthdate():
    # Get and validate user input
    
def calculate_minutes(birthdate):
    # Calculate age in minutes
    
def minutes_to_words(minutes):
    # Convert minutes to English words
    
if __name__ == "__main__":
    main()
```

### Key Functions

#### `get_birthdate()`
- Prompts user for birthdate
- Validates YYYY-MM-DD format
- Returns a `date` object or exits on invalid input

#### `calculate_minutes(birthdate)`
- Uses `datetime.date.today()` to get current date
- Calculates time difference in days
- Converts to minutes (days × 24 × 60)
- Handles leap years automatically

#### `minutes_to_words(minutes)`
- Converts numeric minutes to English words
- Handles large numbers (thousands, millions)
- Formats output without "and" between words
- Follows the style from the Rent song

## 🧪 Testing

### Manual Testing
The program includes comprehensive manual testing scenarios:
- **One year ago**: Should output "Five hundred twenty-five thousand, six hundred minutes"
- **Two years ago**: Should output "One million, fifty-one thousand, two hundred minutes"
- **Invalid format**: Should exit gracefully with `sys.exit()`

### Automated Testing
Run the test suite with:
```bash
pytest test_seasons.py
```

The test file (`test_seasons.py`) includes:
- **Function-specific tests** for each non-main function
- **Edge case testing** for various date scenarios
- **Error condition testing** for invalid inputs
- **Comprehensive coverage** of all program functionality

## 📱 Usage Examples

### Basic Usage
```bash
$ python seasons.py
Birth date: 1990-01-01
```

### Sample Outputs
- **Birth: 1999-01-01, Today: 2000-01-01**
  - Output: "Five hundred twenty-five thousand, six hundred minutes"

- **Birth: 2001-01-01, Today: 2003-01-01**
  - Output: "One million, fifty-one thousand, two hundred minutes"

- **Birth: 1995-01-01, Today: 2000-01-01**
  - Output: "Two million, six hundred twenty-nine thousand, four hundred forty minutes"

## 🔧 Technical Requirements

### Dependencies
- **Python 3.10+** (required for check50 compatibility)
- **datetime** module (built-in)
- **sys** module (built-in)
- **pytest** (for testing)

### File Structure
```
seasons_of_love/
├── seasons.py          # Main program
├── test_seasons.py     # Test suite
└── README.md          # This file
```

## 🎓 CS50 Integration

### Problem Set 8: Object-Oriented Programming
This project is part of CS50's Introduction to Programming with Python, specifically focusing on:
- **Object-oriented programming** principles
- **Advanced Python concepts** and best practices
- **Professional code structure** and organization
- **Comprehensive testing** methodologies

### Submission
Submit your work using:
```bash
submit50 cs50/problems/2022/python/seasons
```

### Verification
Check your code using:
```bash
check50 cs50/problems/2022/python/seasons
```

## 🌟 Key Learning Outcomes

1. **Date and Time Manipulation**: Mastered working with Python's datetime module
2. **Input Validation**: Implemented robust error handling for user inputs
3. **Number-to-Word Conversion**: Created algorithms for converting large numbers to English text
4. **Modular Programming**: Designed clean, maintainable code structure
5. **Testing Practices**: Developed comprehensive test suites for reliable code
6. **Professional Standards**: Followed CS50's coding conventions and best practices

## 🎭 Inspiration

This project draws inspiration from the musical *Rent* and its iconic song "Seasons of Love," which asks the profound question: *"How do you measure a year?"* The program provides a computational answer while maintaining the poetic spirit of the original question.

## 📚 Resources

- [Python datetime documentation](https://docs.python.org/3/library/datetime.html#date-objects)
- [CS50 Python Course](https://cs50.harvard.edu/python/2022/)
- [pytest documentation](https://docs.pytest.org/)

---

*"Five hundred twenty-five thousand, six hundred minutes... How do you measure, measure a year?"* 🎵
