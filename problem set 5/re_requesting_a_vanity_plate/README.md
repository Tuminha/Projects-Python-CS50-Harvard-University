# 🎓 CS50 Python Programming Projects 🐍

Welcome to my CS50 Python Programming journey! This repository contains my solutions and projects for the Harvard University's CS50 Python course.

## 📚 Projects

### Re-requesting a Vanity Plate 🚗

#### 📂 Location
`problem set 5/re_requesting_a_vanity_plate/plates.py` and `test_plates.py`

#### 🎯 Goal
The goal of this project is to implement and thoroughly test a function that validates vanity plate numbers, introducing unit testing concepts with pytest.

#### 📝 Description
This project consists of two parts: implementing a function that checks if a vanity plate meets specific requirements (reimplemented from Problem Set 2) and creating comprehensive tests to verify its functionality. It demonstrates test-driven development and unit testing practices in Python.

#### 🔑 Key Features
- Implementation of vanity plate validation function (`is_valid`)
- Comprehensive test suite using pytest
- Tests for various plate requirements:
  - Length between 2 and 6 characters
  - Starts with two letters
  - Numbers must be at the end and not start with '0'
  - Only alphanumeric characters allowed
- Test-driven development approach

#### 🖥️ How to Run
1. Install pytest:
   ```
   pip install pytest
   ```
2. Navigate to the project directory:
   ```
   cd "problem set 5/re_requesting_a_vanity_plate"
   ```
3. Run the tests:
   ```
   pytest test_plates.py
   ```
4. Run the main program:
   ```
   python plates.py
   ```

#### 🧪 Testing
The test suite includes various test cases:
- Test for valid length → "AA" and "ABCDEF" should be valid
- Test for starting letters → "A2" and "2A" should be invalid
- Test for number placement → "AAA222" should be valid, "AAA22A" should be invalid
- Test for special characters → "CS.50" should be invalid

#### 💡 What I Learned
- Writing unit tests with pytest
- Test-driven development principles
- Function testing strategies
- Handling string validation logic
- Importance of edge cases in testing

#### 🏆 Achievements
This project passed all tests from `check50 cs50/problems/2022/python/tests/plates`, demonstrating both correct implementation and thorough testing practices.

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

Happy coding and driving! 🚗✅
