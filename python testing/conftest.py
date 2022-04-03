import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request, browser_name=None):
    request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service("C:\geckodriver-v0.30.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    elif browser_name == "edge":
        s = Service("C:\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=s)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    print(driver.title)
    print(driver.current_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
