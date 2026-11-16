# Coverage Lab: Looking Beyond Passing Tests

In this lab, I practiced using coverage reports to see which parts of a program my tests actually exercise. I compared a small set of tests with a broader set for shipping costs and user access. The goal was to understand why passing tests alone do not tell us whether important cases have been checked.

## What Is in the Folder

- `shipping.py` calculates shipping costs, applies an express multiplier and a heavy-item surcharge, and checks whether an order qualifies for free shipping.
- `test_shipping.py` checks basic and express shipping.
- `test_shipping_complete.py` adds checks for negative weight, heavy items, and free-shipping eligibility.
- `access.py` grants access only when the user is an active admin.
- `test_access_weak.py` checks two combinations of role and activity status.
- `test_access_complete.py` checks all four combinations: active/inactive admins and active/inactive non-admins.

## Running the Tests

Open a terminal in `coverage-lab`. Install the testing tools if needed:

```bash
python -m pip install pytest pytest-cov
```

Run all tests:

```bash
python -m pytest -v
```

To compare the smaller and broader test sets, run them separately:

```bash
python -m pytest test_shipping.py test_access_weak.py -v
python -m pytest test_shipping_complete.py test_access_complete.py -v
```

## Checking Coverage

Measure coverage of both application modules, including branches, and generate terminal and HTML reports:

```bash
python -m pytest --cov=shipping --cov=access --cov-branch --cov-report=term-missing --cov-report=html
```

Open `htmlcov/index.html` in a browser to explore the report. Line coverage shows which executable lines ran; branch coverage checks the different paths through decisions. For the access rule, testing all four input combinations also helps check each part of the condition.

## Current Test Result

The verified run finished with **12 passed and 1 failed**. The failing test is `test_free_shipping_eligible` in `test_shipping_complete.py`:

```python
assert free_shipping_eligible(1500) == False
```

The function returns `True` because orders of 1,000 or more qualify for free shipping. This assertion therefore disagrees with the current rule. If that rule is intended, the expected result for 1,500 should be `True`; an order below 1,000 can be used to test an ineligible case.

My main takeaway was that coverage helps identify gaps, but it does not prove that a test's expected result is correct. We still need to review the assertions and check relevant boundary cases.
