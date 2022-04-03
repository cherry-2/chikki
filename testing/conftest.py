import pytest


@pytest.fixture()
def setup():
    print("i'm getting first executed")
    yield
    print("i'll finally executed")


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def DataLoad(request):
    return request.param


