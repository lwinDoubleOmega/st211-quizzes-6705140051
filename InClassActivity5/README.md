# In-Class Activity 5: Parameterized Tests

In this activity, I practiced using `pytest.mark.parametrize` to run the same test with different inputs. Instead of writing a separate test for every case, I could keep the test logic in one place and supply several sets of values.

The examples cover even and odd numbers, factorials, and discount calculations. I also tested invalid discount percentages to check that they raise a `ValueError`.

## What I Practiced

- Running one test with several inputs and expected results.
- Combining two parameter lists to test every combination of their values.
- Testing dictionaries and seeing pytest's default test IDs.
- Giving test cases readable names with `pytest.param`.
- Marking a specific case as an expected failure with `xfail`.

`mathutils.py` contains the even-number and factorial functions, while `discount.py` contains the discount calculation. The `test_*.py` files demonstrate the different testing approaches.

## Running the Tests

From this folder, run:

```bash
python -m pytest -v
```

To see the printed values in the combination test, run:

```bash
python -m pytest test_multi.py -v -s
```

The recorded test run finished with **38 passed and 1 xfailed**. The expected failure is the `known_bug` case in `test_param_marks.py`, which deliberately expects an incorrect result for `5 ** 2`.
