from asyncio import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class loginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, user_text, password_text):
        user = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")

        self.send_keys_over_element(user, user_text)
        self.send_keys_over_element(password, password_text)
        login_btn.click()
        sleep(3)

    def send_keys_over_element(self, element, pattern):
        element.click()
        element.clear()
        element.send_keys(pattern)
