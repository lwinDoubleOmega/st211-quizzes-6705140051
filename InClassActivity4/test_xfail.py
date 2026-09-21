import pytest


pytest.mark.xfail(reason="known bug #123, fix in progress")
def test_known_broken_feature():
    assert 1 == 2  # This test is expected to fail due to a known bug    

@pytest.mark.xfail(reason= "Might pass sometimes")
def test_actually_passes_now():
    assert 1 == 1  # This test will pass