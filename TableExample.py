from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from PageObject.Tests.PageObjectBase import pageObjectBase

base = pageObjectBase()
driver = base.selenium_start("https://demo.applitools.com/app.html")

table = driver.find_element(By.CSS_SELECTOR, 'table[class="table table-padded"]')
print(table.text)
rows = table.find_elements(By.TAG_NAME, 'tr')
row = rows[1]
cells = row.find_elements(By.TAG_NAME, 'td')
cell_to_test = cells[0]
print(cell_to_test.text)
base.selenium_end(driver)
