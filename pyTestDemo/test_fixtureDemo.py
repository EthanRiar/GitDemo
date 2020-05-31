import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print('I will execute steps in fixtureDemo method')

    def test_fixtureDemo(self):
        print('I will execute steps in fixtureDemo1 method')

    def test_fixtureDemo(self):
        print('I will execute steps in fixtureDemo2 method')

    def test_fixtureDemo(self):
        print('I will execute steps in fixtureDemo3 method')
