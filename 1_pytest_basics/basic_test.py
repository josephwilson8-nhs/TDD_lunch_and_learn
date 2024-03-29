import pytest
from basic import return_true, add_10, throw_error


def test_return_true():
    """
    Tests if the return_true function returns true
    """
    assert return_true()


def test_return_true_fail():
    """
    Tests if return_rue returns false
    """
    assert return_true() == False


def test_add_10():
    """
    Tests if the add_10 adds 10 to the input
    """
    num = -10
    test_num1 = add_10(num)
    assert test_num1 == 0

    test_num2 = add_10(test_num1)
    assert test_num2 == 10

    test_num3 = add_10(test_num2)
    assert test_num3 == 20


def test_add_10_fail():
    """
    Tests if the add_10 adds 10 to the input. Fails on the second assertion.
    """
    num = -10
    test_num1 = add_10(num)
    assert test_num1 == 0

    test_num2 = add_10(test_num1)
    assert test_num2 != 10

    test_num3 = add_10(test_num2)
    assert test_num3 == 20


def test_throws_error():
    """
    Checks that the throws_error function throws a ValueError
    """
    with pytest.raises(ValueError):
        throw_error()
