import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
list1 =[]
list2= []
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search for Vegetables and Fruits"]').send_keys('ber')
time.sleep(4)
vegetables = driver.find_elements(By.CSS_SELECTOR, 'h4.product-name')

for veg in vegetables:
    list1.append(veg.text)

buttons = driver.find_elements(By.XPATH, '//div[@class="product-action"]/button')
for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()
time.sleep(2)
fruits = driver.find_elements(By.XPATH, '//p[@class="product-name"]')
for fruit in fruits:
    list2.append(fruit.text)

print(list1)
print(list2)
assert list1 == list2
amounts = driver.find_elements(By.XPATH, '//tr/td[5]/p')
Total = 0
for amount in amounts:
    Total = Total + int(amount.text)
print(Total)
TotalAmt = driver.find_element(By.CSS_SELECTOR, 'span.totAmt')
assert Total == int(TotalAmt.text)
driver.find_element(By.CLASS_NAME, 'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()
time.sleep(10)
AmtDisc = float(driver.find_element(By.CSS_SELECTOR, 'span.discountAmt').text)
assert float(Total - Total/10) == AmtDisc
print(AmtDisc)
driver.find_element(By.XPATH, '//button[text()="Place Order"]').click()
driver.find_element(By.XPATH, '//select[@style="width: 200px;"]').send_keys("India")
driver.find_element(By.CSS_SELECTOR, 'input.chkAgree').click()
driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()
driver.close()