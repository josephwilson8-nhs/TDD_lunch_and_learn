"""
To pass multiple arguments to the test function when parametrising a test, 
you can "zip" multiple lists together into a list of tuples. If there is an uneven 
amount of items in a list (nums has 5, outputs has only 4) then the left over values 
will be ignored.
"""
import pytest
from parameterization import timesby_11

nums = [1, 2, 3, 4, 5]
outputs = [11, 22, 35, 44]


@pytest.mark.parametrize("num, output", zip(nums, outputs))
def test_timesby_11(num, output):
    """Test timesby_11 with a set num and output"""
    assert timesby_11(num) == output
