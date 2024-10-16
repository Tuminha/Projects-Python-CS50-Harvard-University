# 🎓 CS50 Python Programming Projects 🐍

Welcome to my CS50 Python Programming journey! This repository contains my solutions and projects for the Harvard University's CS50 Python course.

## 📚 Projects

### Fuel Gauge ⛽

#### 📂 Location
`problem set 3/fuel_gauge/fuel.py`

#### 🎯 Goal
The goal of this project is to create a program that simulates a fuel gauge, converting fractions to percentages and handling special cases for nearly empty and full tanks.

#### 📝 Description
This program prompts the user for a fraction (in the format X/Y) representing the amount of fuel in a tank. It then outputs the fuel level as a percentage, rounded to the nearest integer. The program also handles special cases:
- If 1% or less fuel remains, it outputs "E" (essentially empty)
- If 99% or more fuel remains, it outputs "F" (essentially full)
- It handles various error cases, such as invalid input, division by zero, and fractions greater than 1

#### 🔑 Key Features
- Prompts the user for a fraction input (X/Y format)
- Converts the fraction to a percentage
- Handles special cases for nearly empty and full tanks
- Implements error handling for invalid inputs
- Continuously prompts the user until valid input is provided

#### 🖥️ How to Run
1. Navigate to the project directory:
   ```
   cd "problem set 3/fuel_gauge"
   ```
2. Run the program:
   ```
   python fuel.py
   ```
3. Enter a fraction when prompted
4. See the fuel level output!

#### 🧪 Testing
You can test the program with various inputs:
- Try "3/4" → should output "75%"
- Try "1/4" → should output "25%"
- Try "4/4" → should output "F"
- Try "0/4" → should output "E"
- Try "4/0" → should handle ZeroDivisionError and prompt again
- Try "three/four" → should handle ValueError and prompt again
- Try "1.5/3" → should handle ValueError and prompt again
- Try "5/4" → should prompt again (fraction > 1)

#### 💡 What I Learned
- Handling and converting fractions in Python
- Implementing robust error handling
- Creating a user-friendly input loop
- Rounding and formatting numerical output
- Modular programming with separate functions for conversion and output

#### 🏆 Achievements
This project passed all tests from `check50 cs50/problems/2022/python/fuel`, demonstrating its correctness and adherence to the project specifications.

---

## 🚀 More to Come!
Stay tuned for more exciting Python projects as I progress through the CS50 course!

## 🙏 Acknowledgements
Thanks to Harvard University and the CS50 team for providing this educational opportunity and for creating practical, real-world programming challenges!

### Contact Information

- **Name:** Francisco Teixeira Barbosa
- **Email:** cisco@periospot.com
- **Personal Portfolio:** [https://franciscodds.framer.ai/](https://franciscodds.framer.ai/)
- **GitHub:** [https://github.com/Tuminha](https://github.com/Tuminha)
- **Twitter/X:** [@Cisco_research](https://x.com/Cisco_research)

Happy coding and may your tank always be full! ⛽🚗
