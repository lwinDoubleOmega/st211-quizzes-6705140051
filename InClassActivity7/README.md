# In-Class Activity 7: Mock Objects and Side Effects

In this activity, I practiced using `unittest.mock.Mock` to isolate code from external services and control what a dependency does during a test. I compared fixed return values with dynamic side effects and used mocks to simulate successful responses and failures.

## What I Practiced

- **Fixed return values:** `test_return_value.py` configures a mock method with `return_value`. Every call returns the same configured value.
- **Exceptions:** `test_side_effect_exception.py` uses `side_effect` to make a mocked login operation raise `ValueError`.
- **Sequential values:** `test_side_effect_list.py` demonstrates that a list assigned to `side_effect` is consumed one item at a time; after the list is exhausted, another call raises `StopIteration`.
- **Function-based behavior:** `test_side_effect_function.py` uses a function as a side effect so the result can depend on the argument passed to the mock.
- **Comparison:** `test_comparison.py` shows that a function-based side effect can transform input, while `return_value` always returns one fixed result.
- **Basic mock objects:** `test_mock_basics.py` demonstrates configured methods, arbitrary method calls, and mock attributes.
- **Payment processing:** `payment.py` contains an `OrderProcessor` that can be tested with a mocked payment gateway instead of a real gateway.

## `return_value` and `side_effect`

Use `return_value` when every call should return the same fixed value:

```python
mock.get_status.return_value = "OK"
```

Use `side_effect` when the mock needs dynamic behavior, such as sequential results, argument-based results, or exceptions:

```python
mock.fetch.side_effect = lambda value: value.upper()
```

## Running the Tests

With Python and `pytest` installed, open a terminal in `InClassActivity7` and run:

```bash
python -m pytest -v
```

To run the side-effect exercises only:

```bash
python -m pytest lab_mock_obj/test_side_effect_function.py lab_mock_obj/test_side_effect_exception.py lab_mock_obj/test_side_effect_list.py -v
```

The main takeaway is that mocks make external behavior predictable, while `side_effect` is useful when a test needs behavior that changes based on calls, inputs, or errors.
