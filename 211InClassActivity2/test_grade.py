import pytest
from grade import letter_grade


def test_boundry_a_grade():
    assert letter_grade(80) == "A"
    assert letter_grade(79) == "B"

def test_boundry_pass_fail():
    assert letter_grade(60) == "C"
    assert letter_grade(59) == "F"

def test_minimum_valid():
    assert letter_grade(0) == "F"

def test_maximum_invalid():
    assert letter_grade(100) == "A"

def test_below_minimum():
    with pytest.raises(ValueError):
        letter_grade(-1)