# In-Class Activity 8: Mocking, Patching, and Verifying Calls

In this activity, I practiced using `unittest.mock` to isolate code from external services and verify how dependencies are used. The tests replace email, weather, payment, and database operations with predictable mock objects.

## What I Practiced

- **Patching functions:** `test_notifications.py` patches `notifications.send_email` so the test can exercise `notify_user` without connecting to an SMTP server.
- **Mocking a dependency:** `test_payment.py` gives `OrderProcessor` a fake payment gateway and configures its `change` method to return a successful transaction result.
- **Multiple return values:** `test_return_values.py` uses a list assigned to `side_effect` so successive calls return `1`, `2`, and `3`.
- **Mocking a database:** `test_userService.py` configures `find_user` to return a username without using a real database.
- **Controlling branches:** `test_weather.py` patches `get_temperature` to test both the `Pleasant` and `Cold` branches of `describe_weather`.
- **Verifying calls:** `test_verify_calls.py` demonstrates `assert_called()` and `assert_called_once()` for checking whether a mock method was used.
- **Patching helper functions:** `test_date_utils.py` can replace `get_year` to make the generated report name deterministic.

## Important Mocking Concepts

Use `patch` when a function should be temporarily replaced during a test:

```python
with patch("notifications.send_email") as mock_send:
    mock_send.return_value = True
    result = notify_user("student@siam.ac.th")
```

Use a `Mock` object when a class or service dependency should be supplied directly:

```python
fake_gateway = Mock()
fake_gateway.change.return_value = "SUCCESS-12345"
```

Use `side_effect` when calls need different results or custom behavior:

```python
mock.next_id.side_effect = [1, 2, 3]
```

Common call assertions include:

```python
mock.save.assert_called()
mock.save.assert_called_once()
```

`assert_called_once()` only succeeds when the method has been called exactly once. In `test_verify_calls.py`, the same `save` method is called twice before this assertion, so that test intentionally demonstrates a failure and is not expected to pass as written.

## Running the Tests

Open a terminal in `InClassActivity8` and run the activity tests with:

```bash
python -m pytest -v
```

To run the examples that should pass without the intentional call-count failure:

```bash
python -m pytest test_date_utils.py test_notifications.py test_payment.py test_return_values.py test_userService.py test_weather.py -v
```

The main takeaway is that mocks make unit tests isolated and repeatable: external services do not need to be available, and tests can explicitly control return values, errors, branches, and call counts.
