import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestEndTOEnd(BaseClass):
    def test_etoe(self):
        list1 = []
        list2 = []
        self.driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search for Vegetables and Fruits"]').send_keys('ber')
        time.sleep(4)
        vegetables = self.driver.find_elements(By.CSS_SELECTOR, 'h4.product-name')

        for veg in vegetables:
            list1.append(veg.text)

        buttons = self.driver.find_elements(By.XPATH, '//div[@class="product-action"]/button')
        for button in buttons:
            button.click()
        self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()
        time.sleep(2)
        fruits = self.driver.find_elements(By.XPATH, '//p[@class="product-name"]')
        for fruit in fruits:
            list2.append(fruit.text)

        print(list1)
        print(list2)
        assert list1 == list2
        amounts = self.driver.find_elements(By.XPATH, '//tr/td[5]/p')
        Total = 0
        for amount in amounts:
            Total = Total + int(amount.text)
        print(Total)
        TotalAmt = self.driver.find_element(By.CSS_SELECTOR, 'span.totAmt')
        assert Total == int(TotalAmt.text)
        self.driver.find_element(By.CLASS_NAME, 'promoCode').send_keys("rahulshettyacademy")
        self.driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()
        time.sleep(10)
        AmtDisc = float(self.driver.find_element(By.CSS_SELECTOR, 'span.discountAmt').text)
        assert float(Total - Total/10) == AmtDisc
        print(AmtDisc)
        self.driver.find_element(By.XPATH, '//button[text()="Place Order"]').click()
        self.driver.find_element(By.XPATH, '//select[@style="width: 200px;"]').send_keys("India")
        self.driver.find_element(By.CSS_SELECTOR, 'input.chkAgree').click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()
