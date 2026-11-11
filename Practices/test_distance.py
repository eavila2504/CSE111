#distance.py
from distance import kms_from_miles 
from pytest import approx
import pytest
def test_kms_from_miles():
    """Test the kms_from_miles function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating-point numbers.
    """
    assert kms_from_miles(0) == approx(0)
    assert kms_from_miles(1) == approx(1.60934)
    assert kms_from_miles(5) == approx(8.0467)
    assert kms_from_miles(10) == approx(16.0934)