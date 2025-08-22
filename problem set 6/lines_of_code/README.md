# Problem Set 6 — Lines of Code (lines.py)

Count the number of lines of code in a Python file, excluding blank lines and comments.

## Requirements
- Exit with an error if:
  - No filename is provided, more than one argument is provided, or the filename does not end with `.py`.
  - The file does not exist.
- Only count lines that contain actual code (i.e., non-empty after stripping whitespace and not starting with `#`).

## Approach
- Read the file.
- For each line, `strip()` to remove surrounding whitespace.
- Skip if the line is empty or begins with `#`.
- Count the remaining lines and print the total.

## Usage
From this directory:

```bash
python3 lines.py lines.py           # example usage
```

## Automated Tests
Use CS50's testing tool:

```bash
python3 -m check50 cs50/problems/2022/python/lines
```

## Submission
If your CLI submit tool is set up:

```bash
python3 -m submit50 cs50/problems/2022/python/lines
```

Alternatively, submit via the CS50 web interface at https://submit.cs50.io/ (select the assignment and upload `lines.py`).

## Notes
- This solution intentionally ignores blank lines and full-line `#` comments. Docstrings may be treated as non-comment text per the spec's tests.
- Implemented on macOS with Python 3.x.
