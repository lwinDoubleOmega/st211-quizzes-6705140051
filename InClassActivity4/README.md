# In-Class Activity 4: Pytest Markers

This activity explores how `pytest` markers can organize and control tests. It includes smoke, slow, and regression markers, along with examples of skipped tests and tests expected to fail. The `pytest.ini` file registers the custom markers and enables strict marker checking.

To run everything from this folder:

```bash
python -m pytest
```

To run only the smoke tests:

```bash
python -m pytest -m smoke
```

The full suite is not expected to pass as written: `test_strict.py` uses an unregistered marker to demonstrate strict-marker errors, and one failing test in `test_xfail.py` is missing the `@` that would apply its expected-failure marker.
