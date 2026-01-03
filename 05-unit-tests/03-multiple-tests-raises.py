import pytest
from square_calculator import square

"""
If you put many assertions inside a single test function,
pytest will stop executing that test as soon as it encounters
the first failing assertion.

As a result, any other potential failures inside the same test
will not be reported.

To avoid this, it is better to split assertions into multiple
test functions. This allows pytest to run each test independently
and report all failures instead of stopping at the first one.
"""


def test_positive():
    assert square(2) == 4
    assert square(3) == 9   

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
