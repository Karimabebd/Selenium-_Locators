# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.bdeb.qc.ca/")
driver.maximize_window()

time.sleep(5)
print(driver.title)
driver.get("https://pypi.org/project/webdriver-manager/")
time.sleep(3)
driver.back()
print(driver.current_url)
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.forward()
print(driver.page_source)
driver.close()