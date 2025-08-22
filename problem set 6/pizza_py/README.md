# Problem Set 6 — Pizza Py (pizza.py)

Render Pinocchio’s pizza menu (CSV) as an ASCII table.

## Requirements
- Expect exactly one CLI argument: the CSV file path in the course’s format (e.g., `sicilian.csv` or `regular.csv`).
- If arg count is not 1 → exit with:
  - `Too few command-line arguments` (0 args)
  - `Too many command-line arguments` (>1 arg)
- If filename doesn’t end with `.csv` → `Not a CSV file`.
- If file does not exist → `File does not exist`.
- Print the menu as an ASCII table using `tabulate` with `tablefmt="grid"`.

## Approach
- Validate CLI args with `sys.argv`.
- Use `csv.DictReader` to parse the header and rows.
- Materialize rows into a list and pass to `tabulate(rows, headers="keys", tablefmt="grid")`.
- Wrap file opening in `try/except FileNotFoundError` and exit with the required message.

## Usage
From this directory:

```bash
pip install tabulate  # once
python3 pizza.py sicilian.csv
python3 pizza.py regular.csv
```

## Example Output
```
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
```

## Automated Tests
```bash
python3 -m check50 cs50/problems/2022/python/pizza
```

## Submission
```bash
python3 -m submit50 cs50/problems/2022/python/pizza
```

## Notes
- Prefer `csv.DictReader` + `headers="keys"` for clean integration with `tabulate`.
- Avoid iterating a CSV reader twice; collect rows before printing.
- Ensure messages match the spec exactly.
