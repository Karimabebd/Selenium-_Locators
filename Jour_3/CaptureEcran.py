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
driver.get("https://www.selenium.dev/documentation/overview/components/")
#driver.save_screenshot("C:\\Users\\User\\selemiumProjet\\Jour_3\\selenium.png")
driver.save_screenshot(os.getcwd()+"\\selenium1.png")

time.sleep(5)
driver.close()

