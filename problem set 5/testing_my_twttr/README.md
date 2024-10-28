# 🎓 CS50 Python Programming Projects 🐍

Welcome to my CS50 Python Programming journey! This repository contains my solutions and projects for the Harvard University's CS50 Python course.

## 📚 Projects

### Testing my twttr 🧪

#### 📂 Location
`problem set 5/testing_my_twttr/test_twttr.py` and `twttr.py`

#### 🎯 Goal
The goal of this project is to implement and thoroughly test a function that removes vowels from text, introducing unit testing concepts with pytest.

#### 📝 Description
This project consists of two parts: implementing a function that removes vowels from text (reimplemented from Problem Set 2) and creating comprehensive tests to verify its functionality. It demonstrates test-driven development and unit testing practices in Python.

#### 🔑 Key Features
- Implementation of vowel removal function (`shorten`)
- Comprehensive test suite using pytest
- Tests for various input cases:
  - Lowercase vowels
  - Uppercase vowels
  - Mixed case strings
  - Numbers and special characters
  - Empty strings
- Test-driven development approach

#### 🖥️ How to Run
1. Install pytest:
   ```
   pip install pytest
   ```
2. Navigate to the project directory:
   ```
   cd "problem set 5/testing_my_twttr"
   ```
3. Run the tests:
   ```
   pytest test_twttr.py
   ```
4. Run the main program:
   ```
   python twttr.py
   ```

#### 🧪 Testing
The test suite includes various test cases:
- Test with simple words: "hello" → "hll"
- Test with uppercase: "HELLO" → "HLL"
- Test with punctuation: "hello, world!" → "hll, wrld!"
- Test with numbers: "CS50" → "CS50"
- Test with mixed case: "Python" → "Pythn"

#### 💡 What I Learned
- Writing unit tests with pytest
- Test-driven development principles
- Function testing strategies
- Code organization for testability
- Importance of edge cases in testing

#### 🏆 Achievements
This project passed all tests from `check50 cs50/problems/2022/python/tests/twttr`, demonstrating both correct implementation and thorough testing practices.

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

Happy coding and testing! 🧪✅

