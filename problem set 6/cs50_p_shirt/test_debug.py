#!/usr/bin/env python3

import sys
print(f"Number of arguments: {len(sys.argv)}")
print(f"Arguments: {sys.argv}")

if len(sys.argv) != 3:
    print("Too few command-line arguments")
    sys.exit(1)
else:
    print("Correct number of arguments")

