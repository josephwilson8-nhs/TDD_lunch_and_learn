import pytest
from fixtures import add_5
from define_fixtures import num_5


@pytest.fixture()
def num_10():
    """Return 10"""
    return 10


def test_add_10_to_num_10(num_10):
    """
    Tests if the add_10 adds 10 to the input, starting with 10
    """
    test_num1 = add_5(num_10)
    assert test_num1 == 15

    test_num2 = add_5(test_num1)
    assert test_num2 == 20

    test_num3 = add_5(test_num2)
    assert test_num3 == 25


def test_add_10_to_num_5(num_5):
    """
    Tests if the add_10 adds 10 to the input, starting with 5
    """
    test_num1 = add_5(num_5)
    assert test_num1 == 10

    test_num2 = add_5(test_num1)
    assert test_num2 == 15

    test_num3 = add_5(test_num2)
    assert test_num3 == 20
