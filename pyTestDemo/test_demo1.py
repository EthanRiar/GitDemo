import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondgreetCreditCard():
    print("Good Mornng")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])