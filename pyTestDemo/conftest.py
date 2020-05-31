import pytest


@pytest.fixture(scope="class")
def setup():
    print('I will be executed first')
    yield
    print('I will be executed last')


@pytest.fixture()
def dataLoad():
    print("user profile data is being create")
    return ["Barinder", "Riar", "facebook.com"]


@pytest.fixture(params=[("chrome","Barinder"),"Firefox","IE"])
def crossBrowser(request):
    return request.param

