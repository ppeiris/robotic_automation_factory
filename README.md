# Robotic Automation Factory - Package Sorting

> **Note from the author:** This code has been generated using [Claude Code](https://claude.ai/code) with prompts and is well tested with comprehensive edge case coverage.

## Problem

Imagine you work in Smarter Technology's robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Implementation

Implement the function **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.

## Solution

The solution is implemented in Python in [`sort.py`](sort.py).

```python
def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
```

### Approach

1. **Calculate volume** from the three dimensions.
2. **Determine bulky**: check if volume >= 1,000,000 cm³ or any single dimension >= 150 cm.
3. **Determine heavy**: check if mass >= 20 kg.
4. **Dispatch** based on the combination:
   - Both bulky and heavy → `REJECTED`
   - Either bulky or heavy → `SPECIAL`
   - Neither → `STANDARD`

## Running

### Prerequisites

- Python 3.x
- pytest (`pip install pytest`)

### Run Tests

```bash
pytest test_sort.py -v
```

### Run Directly

```bash
python sort.py
```
