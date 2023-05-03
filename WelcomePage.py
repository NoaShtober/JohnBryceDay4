from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class welcomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        sub_title = self.driver.find_element(By.CSS_SELECTOR, "span[class= 'title']")
        act_title = sub_title.text
        assert act_title == 'Products', 'Product page is not as expected'

    def searchAplitools(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder=" Start typing to search..."]')
        self.send_keys_over_element(search_box, "cat")

    def Welcome(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return prices



    def send_keys_over_element(self, element, pattern):
        element.click()
        element.clear()
        element.send_keys(pattern)

