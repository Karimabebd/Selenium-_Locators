import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
#driver.get("https://www.selenium.dev/documentation/overview/components/")
#le nom de link text est le meme
#driver.find_element(By.LINK_TEXT, "Watch the Videos").click()
#le nom de link text est pas le meme
#driver.find_element(By.PARTIAL_LINK_TEXT, "the Videos").click()
#exemple

driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click()

time.sleep(5)
driver.close()
