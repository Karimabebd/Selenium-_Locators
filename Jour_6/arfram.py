import pytest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver
def test_iframe():
   driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
   driver.switch_to.frame("packageListeFrame")
   driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
   time.sleep(5)



time.sleep(4)
driver.quit()
