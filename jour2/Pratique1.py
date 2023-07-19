import time
# importer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://espacepourlavie.ca/biodome")

time.sleep(3)
#-----------erreur voir avec rabeh
#driver.find_element(By.XPATH, "//div[@class='green-button']").click()

driver.find_elements(By.XPATH, "[//a[@id='ic-twitter']").click()
#------------
# footer=driver.find_element(By.CLASS_NAME,"")green-button
# driver.find_element(By.ID,"ic-twitter")
# Twiter=driver.find_element(By.ID,"ic-twitter")
# print(Twiter)
#
# driver.title
time.sleep(4)
driver.quit()