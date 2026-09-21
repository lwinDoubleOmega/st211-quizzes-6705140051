from pytest import approx

def test_float_precision():
    assert 0.1 + 0.2 == approx(0.3)

def test_float_with_approx_fails():
    assert 0.1 + 0.2 != approx(0.3)  # This will fail