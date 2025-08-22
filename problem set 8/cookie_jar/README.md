# 🍪 Cookie Jar

## 📖 Project Overview

**Cookie Jar** is a Python program that implements a `Jar` class to simulate a cookie jar with a specified capacity. The program allows users to deposit and withdraw cookies while maintaining proper validation and error handling. The jar can only hold a limited number of cookies, and operations that exceed capacity or attempt to withdraw more cookies than available will raise appropriate errors.

## 🎯 Learning Objectives

This project focuses on:
- **Object-Oriented Programming** concepts and class design
- **Properties and Decorators** using `@property` and `@setter`
- **Input Validation** and error handling with custom exceptions
- **String Representation** and custom `__str__` methods
- **Unit Testing** with pytest
- **Data Encapsulation** and private attributes
- **Method Implementation** for deposit and withdraw operations

## 🚀 Features

### Core Functionality
- **Cookie Jar Management**: Create a jar with specified capacity
- **Deposit Cookies**: Add cookies to the jar (with capacity validation)
- **Withdraw Cookies**: Remove cookies from the jar (with availability validation)
- **Capacity Validation**: Ensures capacity is always positive
- **Size Tracking**: Maintains current number of cookies in the jar
- **Visual Representation**: Displays cookies as emoji characters

### Technical Features
- **Property Decorators**: Uses `@property` for controlled access to attributes
- **Input Validation**: Rejects negative capacity and invalid operations
- **Error Handling**: Raises `ValueError` with descriptive messages
- **Private Attributes**: Uses `_capacity` and `_size` for internal storage
- **Comprehensive Testing**: Full test suite covering all functionality

## 🛠️ Implementation Details

### Class Structure
```python
class Jar:
    def __init__(self, capacity=12):
        # Initialize jar with capacity validation
        
    def __str__(self):
        # Return visual representation of cookies
        
    def deposit(self, n):
        # Add cookies with capacity check
        
    def withdraw(self, n):
        # Remove cookies with availability check
        
    @property
    def capacity(self):
        # Read-only access to capacity
        
    @property
    def size(self):
        # Read-only access to current size
```

### Key Methods

#### `__init__(self, capacity=12)`
- Initializes jar with specified capacity (default: 12)
- Validates that capacity is positive
- Sets initial size to 0
- Raises `ValueError` for invalid capacity

#### `deposit(self, n)`
- Adds `n` cookies to the jar
- Validates that deposit won't exceed capacity
- Raises `ValueError` if capacity would be exceeded

#### `withdraw(self, n)`
- Removes `n` cookies from the jar
- Validates that enough cookies are available
- Raises `ValueError` if insufficient cookies

#### `__str__(self)`
- Returns visual representation using cookie emojis (🍪)
- Empty jar returns empty string
- Filled jar shows appropriate number of cookies

## 🧪 Testing

### Manual Testing
The program includes comprehensive manual testing scenarios:
- **Valid Capacity**: Create jar with positive capacity
- **Invalid Capacity**: Attempt to create jar with negative capacity
- **Deposit Operations**: Add cookies within and beyond capacity
- **Withdraw Operations**: Remove cookies with sufficient and insufficient availability
- **String Representation**: Verify emoji display for different sizes

### Automated Testing
Run the test suite with:
```bash
pytest test_jar.py
```

The test file (`test_jar.py`) includes:
- **Initialization Tests**: Verify proper jar creation and validation
- **String Representation Tests**: Check emoji display accuracy
- **Deposit Tests**: Validate deposit operations and capacity limits
- **Withdraw Tests**: Ensure proper withdrawal behavior and error handling

## 📱 Usage Examples

### Basic Usage
```python
from jar import Jar

# Create a jar with default capacity (12)
jar = Jar()

# Create a jar with custom capacity
jar = Jar(20)

# Deposit cookies
jar.deposit(5)

# Withdraw cookies
jar.withdraw(2)

# Check current state
print(f"Size: {jar.size}, Capacity: {jar.capacity}")
print(jar)  # Shows: 🍪🍪🍪
```

### Sample Outputs
- **Empty Jar**: `""` (no cookies)
- **One Cookie**: `"🍪"`
- **Full Jar (12 cookies)**: `"🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"`

### Error Scenarios
- **Negative Capacity**: `ValueError: Capacity must be positive`
- **Exceed Capacity**: `ValueError: Exceeded capacity`
- **Insufficient Cookies**: `ValueError: Not enough cookies`

## 🔧 Technical Requirements

### Dependencies
- **Python 3.10+** (required for check50 compatibility)
- **pytest** (for testing)

### File Structure
```
cookie_jar/
├── jar.py           # Main Jar class implementation
├── test_jar.py      # Test suite
└── README.md        # This file
```

## 🎓 CS50 Integration

### Problem Set 8: Object-Oriented Programming
This project is part of CS50's Introduction to Programming with Python, specifically focusing on:
- **Object-oriented programming** principles
- **Class design** and implementation
- **Property decorators** and data encapsulation
- **Input validation** and error handling
- **Comprehensive testing** methodologies

### Submission
Submit your work using:
```bash
submit50 cs50/problems/2022/python/cookie_jar
```

### Verification
Check your code using:
```bash
check50 cs50/problems/2022/python/cookie_jar
```

## 🌟 Key Learning Outcomes

1. **Class Design**: Mastered creating classes with proper initialization and validation
2. **Property Decorators**: Implemented controlled access to class attributes using `@property`
3. **Input Validation**: Created robust error handling for invalid inputs and operations
4. **String Representation**: Implemented custom `__str__` method for visual output
5. **Data Encapsulation**: Used private attributes with public property access
6. **Testing Practices**: Developed comprehensive test suites for reliable code
7. **Error Handling**: Implemented proper exception handling with descriptive messages

## 🍪 Cookie Jar Logic

The Cookie Jar implements a simple but effective storage system:
- **Capacity**: Maximum number of cookies the jar can hold
- **Size**: Current number of cookies in the jar
- **Deposit**: Add cookies (cannot exceed capacity)
- **Withdraw**: Remove cookies (cannot go below 0)
- **Visual**: Emoji representation for easy understanding

## 📚 Resources

- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Python Properties](https://docs.python.org/3/library/functions.html#property)
- [CS50 Python Course](https://cs50.harvard.edu/python/2022/)
- [pytest documentation](https://docs.pytest.org/)

---

*"A cookie jar that's both functional and fun! 🍪✨"*
