# Problem Set 6 — Scourgify (scourgify.py)

Clean and reformat CSV data by splitting combined names into separate first/last columns.

## Requirements
- Expect exactly two CLI arguments: input CSV path and output CSV path.
- Input CSV has columns: `name` (format: "last, first"), `house`.
- Output CSV should have columns: `first`, `last`, `house`.
- Exit with error if:
  - Wrong number of arguments → `Too few/many command-line arguments`.
  - Input file doesn't exist → `Could not read [filename]`.

## Approach
- Validate CLI args count and input file existence.
- Use `csv.DictReader` to parse the input CSV, skipping the header.
- Split each `name` field on `", "` to extract `last, first`.
- Write to output using `csv.DictWriter` with new column order.

## Input Format
```csv
name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
```

## Output Format
```csv
first,last,house
Hannah,Abbott,Hufflepuff
Katie,Bell,Gryffindor
```

## Usage
From this directory:

```bash
# Download test data
wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

# Run the program
python3 scourgify.py before.csv after.csv
```

## Testing
```bash
# Manual tests
python3 scourgify.py                    # Too few arguments
python3 scourgify.py 1.csv 2.csv 3.csv # Too many arguments
python3 scourgify.py invalid.csv out.csv # File not found
python3 scourgify.py before.csv after.csv # Success

# Automated tests
python3 -m check50 cs50/problems/2022/python/scourgify
```

## Submission
```bash
python3 -m submit50 cs50/problems/2022/python/scourgify
```

## Notes
- Input names are in "last, first" format with quotes.
- Output columns are reordered: first, last, house.
- Uses `split(",", 1)` to handle names with commas properly.
