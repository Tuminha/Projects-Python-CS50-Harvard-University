# implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, 
# excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file's name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

with open(sys.argv[1], "r") as file:
    lines = file.readlines()

# Filter out blank lines and comment lines
code_lines = []
for line in lines:
    # Remove leading/trailing whitespace
    stripped_line = line.strip()
    # Skip empty lines and comment lines
    if stripped_line and not stripped_line.startswith("#"):
        code_lines.append(line)

print(len(code_lines))
