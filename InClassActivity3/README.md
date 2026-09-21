# In-Class Activity 3: More Ways to Test

In this activity, I practiced positive and negative test cases for email and age validation. I also explored comparing collections, checking floating-point values with `pytest.approx`, and testing a small shopping cart.

The files are grouped by topic: `validators.py` and its positive/negative tests, `shopping.py` and its tests, plus separate examples for collections and floats.

Run the tests from this folder with:

```bash
python -m pytest
```

Some tests currently fail. For example, the shopping-cart class name does not match the name used in its tests, and one float test deliberately checks an incorrect expectation. I have left those examples as part of the exercise.
