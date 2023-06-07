import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/overview/components/")
titrePage=driver.find_element(By.TAG_NAME,"h1").text
print(titrePage)
liens=driver.find_elements(By.TAG_NAME,"a")
print("Le nombre total de liens sur la page est: ", len (liens))
for lien in liens:
    print(lien.text)
time.sleep(5)
driver.close()

