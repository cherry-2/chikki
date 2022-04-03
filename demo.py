import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
# s = Service("C:\\geckodriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Firefox(service=s)
driver.implicitly_wait(10)
list1 = []
list2 = []
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for Vegetables and Fruits"]').send_keys('be')
time.sleep(4)
vegetables = driver.find_elements(By.CSS_SELECTOR, 'h4.product-name')

for veg in vegetables:
    list1.append(veg.text)
print(list1)

buttons = driver.find_elements(By.XPATH, '//div[@class="product-action"]/button')
for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()
time.sleep(8)
fruits = driver.find_elements(By.XPATH, '//p[@class="product-name"]')
for fruit in fruits:
    list2.append(fruit.text)
print(list2)
assert list1 == list2

driver.find_element(By.CLASS_NAME, 'promoCode').send_keys('rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR,'button[class="promoBtn"]').click()
time.sleep(8)
driver.find_element(By.XPATH, '//button[text()="Place Order"]').click()
driver.find_element(By.CSS_SELECTOR,'select[style="width: 200px;"]').send_keys('India')
driver.find_element(By.CLASS_NAME,"chkAgree").click()
time.sleep(2)
driver.find_element(By.TAG_NAME,'button').click()
driver.close() y6
