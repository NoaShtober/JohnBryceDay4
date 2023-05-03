from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class pageObjectBase:

    def selenium_start(self, url):
       driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
       driver.get(url)
       driver.maximize_window()
       driver.implicitly_wait(10)
       return driver

    def selenium_end(self, driver):
        driver.close()
