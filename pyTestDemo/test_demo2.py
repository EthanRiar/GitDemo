import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Failed"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Failed again!!"
