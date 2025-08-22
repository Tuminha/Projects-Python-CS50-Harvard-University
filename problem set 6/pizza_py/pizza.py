# implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
# and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.
# Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

import sys
import csv
from tabulate import tabulate

def main():
    # First thing is to check if the user has provided the correct number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Second thing is to check if the file is a CSV file
    path = sys.argv[1]
    if not path.endswith(".csv"):
        sys.exit("Not a CSV file")
    # In case it's a CSV file, we need to read the file and print the table
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            # Then format the table using the library’s grid format
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Print the table using the library’s grid format           
    print(tabulate(rows, headers="keys", tablefmt="grid"))

# If the program is run directly, call the main function
if __name__ == "__main__":
    main()