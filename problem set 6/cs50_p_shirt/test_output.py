#!/usr/bin/env python3

import sys
import os

# Redirect output to a file
with open('test_output.txt', 'w') as f:
    f.write(f"Number of arguments: {len(sys.argv)}\n")
    f.write(f"Arguments: {sys.argv}\n")
    
    if len(sys.argv) != 3:
        f.write("Too few command-line arguments\n")
        sys.exit(1)
    else:
        f.write("Correct number of arguments\n")

print("Test completed - check test_output.txt")

