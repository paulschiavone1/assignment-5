# assignment-5

# DATA 4000 — Assignment 5

## Description

This repository contains two Python programs for Assignment 5.

- `pos_checkout.py` — A point-of-sale checkout system that calculates item totals, discounts, and a seed-based member perk.
- `inventory_spotcheck.py` — An inventory reorder analyzer that checks stock levels and uses the iTunes Search API to count songs.

Both programs use student-key personalization, loops, conditionals, and input validation.

## Requirements

- Python 3.x
- VS Code
- Internet connection for the API spot check

Install the required library using:

```bash
pip install requests
```

## How to Run

Open the project folder in VS Code and open the terminal.

### Exercise 1: Point-of-Sale Checkout

Run:

```bash
python3 pos_checkout.py
```

Enter your student key, item names, prices, and quantities. Type `DONE` when finished.

Example output:

```text
Seed: 394
Units: 3
Subtotal: $12.00
Discount: 0%
Perk applied: NO
Total: $12.00
```

### Exercise 2: Inventory Reorder Analyzer

Run:

```bash
python3 inventory_spotcheck.py
```

Enter your student key, SKUs, and on-hand quantities. Type `DONE` when finished.

Example output:

```text
Seed: 394
Threshold: 12
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
```

The API example is illustrative. Actual results may vary.

## Files

- `pos_checkout.py`
- `inventory_spotcheck.py`
- `README.md`