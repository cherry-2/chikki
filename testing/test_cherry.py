import pytest


@pytest.mark.xfail
def test_first_programChitki(setup):
    print("fucked up")


@pytest.mark.smoke
def test_first_program1(setup):
    print("yes")


def test_fixturedDemo(setup):
    print ("fixtureDemo got primted")

