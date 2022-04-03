'''from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service("C:\\geckodriver.exe")
driver = webdriver.Firefox(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.close()'''
from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file whi7ch will then #invoke actual browser
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
#to refresh the browser
driver.refresh()
#to close the browser
driver.close()

'''def setup(request):
    s = Service("C:\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    print(driver.title)
    print(driver.current_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()'''

def setup(request):
    s = Service("C:\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=s)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    print(driver.title)
    print(driver.current_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()