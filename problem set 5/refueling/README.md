# 🎓 CS50 Python Programming Projects 🐍

Welcome to my CS50 Python Programming journey! This repository contains my solutions and projects for the Harvard University's CS50 Python course.

## 📚 Projects

### Refueling ⛽

#### 📂 Location
`problem set 5/refueling/fuel.py` and `test_fuel.py`

#### 🎯 Goal
The goal of this project is to implement and thoroughly test a function that converts fuel fractions to percentages and gauges the fuel level, introducing unit testing concepts with pytest.

#### 📝 Description
This project consists of two parts: implementing functions that convert a fuel fraction to a percentage and gauge the fuel level, and creating comprehensive tests to verify their functionality. It demonstrates test-driven development and unit testing practices in Python.

#### 🔑 Key Features
- Implementation of fuel conversion function (`convert`)
- Implementation of fuel gauge function (`gauge`)
- Comprehensive test suite using pytest
- Tests for various fraction and percentage cases:
  - Valid fractions and their percentage conversions
  - Edge cases for empty and full tanks
  - Error handling for invalid fractions

#### 🖥️ How to Run
1. Install pytest:
   ```
   pip install pytest
   ```
2. Navigate to the project directory:
   ```
   cd "problem set 5/refueling"
   ```
3. Run the tests:
   ```
   pytest test_fuel.py
   ```
4. Run the main program:
   ```
   python fuel.py
   ```

#### 🧪 Testing
The test suite includes various test cases:
- Test for typical fractions → "1/2" should return 50%
- Test for edge cases → "0/1" should return "E", "1/1" should return "F"
- Test for invalid fractions → "2/1" should raise ValueError, "1/0" should raise ZeroDivisionError

#### 💡 What I Learned
- Writing unit tests with pytest
- Test-driven development principles
- Function testing strategies
- Handling exceptions in Python
- Importance of edge cases in testing

#### 🏆 Achievements
This project passed all tests from `check50 cs50/problems/2022/python/tests/fuel`, demonstrating both correct implementation and thorough testing practices.

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

Happy coding and refueling! ⛽✅
