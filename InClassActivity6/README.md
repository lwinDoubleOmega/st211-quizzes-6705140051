# In-Class Activity 6: Data-Driven Tests, Fixtures, and Mocking

In this activity, I practiced separating test data from test logic. I loaded cases from JSON and CSV files so the same test could check several inputs without repeating the code. I also explored parameterized fixtures, setup and teardown, and mocking a random value to make a test predictable.

## What I Practiced

- **JSON test data:** `test_data_driven.py` reads `test_cases.json` and checks that each input becomes the expected uppercase text.
- **CSV test data:** `test_csv_driven.py` reads `logins.csv` and tests the validation function in `validate.py`. A login is considered valid here when both the username and password are nonempty.
- **Parameterized fixtures:** `test_param_fixture.py` runs the same test with SQLite, Postgres, and MySQL names.
- **Setup and teardown:** `test_browsers.py` uses a fixture with `yield` to print setup and cleanup messages for Chrome, Firefox, and Safari.
- **Mocking:** `test_solution_preview.py` uses `unittest.mock.patch` to replace the random temperature from `weater.py` and check the Freezing, Cold, Warm, and Hot results.

The browser and database examples use names as sample values; they do not open browsers or connect to real databases.

## Running the Tests

With Python and `pytest` installed, open a terminal in `InClassActivity6` and run:

```bash
python -m pytest -v
```

Run the command from this folder because the data loaders look for `logins.csv` and `test_cases.json` in the current directory.

To see the fixture setup and teardown messages, run:

```bash
python -m pytest test_browsers.py test_param_fixture.py -v -s
```

The main takeaway for me was that reusable fixtures and external test data make tests easier to extend, while mocking lets us check specific outcomes without depending on randomness.
