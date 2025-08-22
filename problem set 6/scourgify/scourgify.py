# The user to provide two command-line arguments:
# The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# The name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

# First import the sys module and the csv module
import sys
import csv
import os

# Then check if the user has provided the correct number of arguments, and in case the number is correct check if the file exists and print error "Could not read [input]..." if the file does not exist
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not os.path.exists(sys.argv[1]):
    sys.exit(f"Could not read {sys.argv[1]}")

# Then read the input file and write the output file
rows = []
with open(sys.argv[1], "r", newline="") as input_file:
    # Use DictReader so the header row is handled for us
    reader = csv.DictReader(input_file)
    for record in reader:
        name = (record.get("name") or "").strip()
        house = (record.get("house") or "").strip()
        try:
            # Input format is "last, first"
            last, first = [part.strip() for part in name.split(",", 1)]
        except ValueError:
            sys.exit("Input file not in the expected format")
        rows.append({"first": first, "last": last, "house": house})

# Write to the output path provided by the user (second CLI argument)
with open(sys.argv[2], "w", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(rows)