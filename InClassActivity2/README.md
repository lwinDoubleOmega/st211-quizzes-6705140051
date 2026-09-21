# In-Class Activity 2: Testing Boundaries and Independence

This activity helped me practice testing small pieces of code in different ways. `grade.py` turns a score into a letter grade, and its tests focus on boundary values such as 59/60 and 79/80. `bank.py` is a simple bank account with deposit and withdrawal methods.

The bank tests also show why test independence matters: `test_bank.py` uses one shared account, while `test_dependencies.py` creates a fresh account for each test.

To run the tests from this folder:

```bash
python -m pytest
```
