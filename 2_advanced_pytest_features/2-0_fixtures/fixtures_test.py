import pytest
from fixtures import add_5

@pytest.fixture()
def num():
    return 10

def test_add_10(num):
    """
    Tests if the add_10 adds 10 to the input
    """
    test_num1 = add_5(num)
    assert test_num1 == 15

    test_num2 = add_5(test_num1)
    assert test_num2 == 20

    test_num3 = add_5(test_num2)
    assert test_num3 == 25
