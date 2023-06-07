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
driver.get("https://www.selenium.dev/documentation/overview/components/")
#POUR nom de text est le meme
driver.find_element(By.LINK_TEXT, "Watch the Videos").click()
#on va resumer le nom text
driver.find_element(By.PARTIAL_LINK_TEXT, " the Videos").click()
# pour recupere la valeur des href et target
attributDuLien = driver.find_element(By.PARTIAL_LINK_TEXT, " the Videos").get_attribute("href")
print(attributDuLien)
attributDuTarget = driver.find_element(By.PARTIAL_LINK_TEXT, " the Videos").get_attribute("target")
print(attributDuTarget)
assert attributDuTarget == "_blank"
driver.find_element(By.LINK_TEXT,"Watch the Videos").is_displayed()
assert attributDuLien == "https://www.youtube.com/playlist?list=PLRdSclUtJDYXDEsWI0vwBmJxW17NgsaAk"
time.sleep(4)
driver.close()