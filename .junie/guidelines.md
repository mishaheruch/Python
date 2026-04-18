# Project Guidelines

This document provides essential information for developers working on this project.

## 1. Build and Configuration

The project consists of independent Python scripts organized by daily tasks (`day01`, `day02`, etc.). There is no global build system or external dependency manager (like `pip`).

### Requirements
- **Python 3.x**: Ensure you have Python 3 installed.
- **Standard Library**: Most scripts rely only on the Python standard library (`os`, `sys`, `json`, `csv`, `datetime`, `collections`).

### Running Scripts
Scripts should be run from the project root or their respective directories. Some scripts expect data in specific locations:
- `day08/analyzes_quantity.py`: Expects a `data` folder in the same directory containing `.csv` files.
- `day07/schedule_cli.py`: Uses `schedule.json` in the current working directory.

## 2. Testing Information

### Test Framework
The project uses the built-in `unittest` framework.

### Running Tests
To run tests, you can execute them directly with Python:
```bash
python3 path/to/test_file.py
```

### Adding New Tests
1. Create a new file prefixed with `test_` or named descriptively (e.g., `temp_test_day08.py`).
2. Import `unittest` and the functions you wish to test.
3. Define a class inheriting from `unittest.TestCase`.
4. Use assertions like `self.assertEqual()`, `self.assertIn()`, etc.

**Note on Imports**: Since the project is not a package, you may need to add the target directory to `sys.path` to import modules correctly:
```python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'day08'))
from analyzes_quantity import parse_date
```

### Example Test
The following test verifies the date parsing logic in `day08/analyzes_quantity.py`:
```python
import unittest
from datetime import datetime
from day08.analyzes_quantity import parse_date

class TestDateParsing(unittest.TestCase):
    def test_iso_format(self):
        self.assertEqual(parse_date("2020-03-01"), datetime(2020, 3, 1))
        
    def test_us_format(self):
        self.assertEqual(parse_date("03/01/2020"), datetime(2020, 3, 1))

if __name__ == '__main__':
    unittest.main()
```

## 3. Additional Development Information

### Code Style
- **Naming**: The project uses `snake_case` for functions and variables (e.g., `parse_date`, `hired_after_count`).
- **Comments**: Comments are occasionally used in Ukrainian/Russian (e.g., `day05/text_analyzer.py`). Maintain the language of existing comments in the respective files.
- **Encoding**: When reading files, scripts often handle multiple encodings (e.g., `utf-8-sig`, `utf-16`, `latin-1`) as seen in `day08/analyzes_quantity.py`.

### Side Effects on Import
Be aware that some scripts (like `day08/analyzes_quantity.py`) execute logic immediately upon being imported. This can cause output to be printed or files to be read during test execution. It is recommended to wrap such logic in `if __name__ == "__main__":` blocks for better testability.
