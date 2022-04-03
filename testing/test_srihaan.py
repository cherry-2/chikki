import pytest


@pytest.mark.smoke
def test_first_program2(setup):
    print("hi")


def test_first_program3Chitki(setup):
    print("good morning")


def test_CrossBrowsers(DataLoad):
    print(DataLoad)