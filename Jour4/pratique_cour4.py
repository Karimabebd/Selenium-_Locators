import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://openclassrooms.com/fr/")
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Démarrer ma candidature").click()
login_URL=driver.current_url
Title_Attendu=driver.title
print(login_URL,"",Title_Attendu)
time.sleep(5)
driver.quit()
