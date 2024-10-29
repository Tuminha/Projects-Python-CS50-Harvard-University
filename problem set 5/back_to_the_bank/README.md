# 🎓 CS50 Python Programming Projects 🐍

Welcome to my CS50 Python Programming journey! This repository contains my solutions and projects for the Harvard University's CS50 Python course.

## 📚 Projects

### Back to the Bank 🏦

#### 📂 Location
`problem set 5/back_to_the_bank/test_bank.py` and `bank.py`

#### 🎯 Goal
The goal of this project is to implement and thoroughly test a function that determines bank rewards based on customer greetings, introducing unit testing concepts with pytest.

#### 📝 Description
This project consists of two parts: implementing a function that assigns monetary values to different types of greetings (reimplemented from Problem Set 1) and creating comprehensive tests to verify its functionality. It demonstrates test-driven development and unit testing practices in Python.

#### 🔑 Key Features
- Implementation of greeting evaluation function (`value`)
- Comprehensive test suite using pytest
- Tests for various greeting cases:
  - "hello" greetings ($0)
  - "h" starting greetings ($20)
  - Other greetings ($100)
- Case-insensitive greeting handling
- Test-driven development approach

#### 🖥️ How to Run
1. Install pytest:
   ```
   pip install pytest
   ```
2. Navigate to the project directory:
   ```
   cd "problem set 5/back_to_the_bank"
   ```
3. Run the tests:
   ```
   pytest test_bank.py
   ```
4. Run the main program:
   ```
   python bank.py
   ```

#### 🧪 Testing
The test suite includes various test cases:
- Test with "hello" greetings → should return 0
- Test with "h" starting words → should return 20
- Test with other greetings → should return 100
- Test case sensitivity → "HELLO" and "hello" should both return 0
- Test complete phrases → "hello, newman" should return 0

#### 💡 What I Learned
- Writing unit tests with pytest
- Test-driven development principles
- Function testing strategies
- Case-insensitive string handling
- Importance of edge cases in testing

#### 🏆 Achievements
This project passed all tests from `check50 cs50/problems/2022/python/tests/bank`, demonstrating both correct implementation and thorough testing practices.

---

## 🚀 More to Come!
Stay tuned for more exciting Python projects as I progress through the CS50 course!

## 🙏 Acknowledgements
Thanks to Harvard University and the CS50 team for providing this educational opportunity and for introducing important software testing concepts!

### Contact Information

- **Name:** Francisco Teixeira Barbosa
- **Email:** cisco@periospot.com
- **Personal Portfolio:** [https://franciscodds.framer.ai/](https://franciscodds.framer.ai/)
- **GitHub:** [https://github.com/Tuminha](https://github.com/Tuminha)
- **Twitter/X:** [@Cisco_research](https://x.com/Cisco_research)

Happy coding and banking! 🏦✅
