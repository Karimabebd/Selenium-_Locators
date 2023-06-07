import time
#on va inporter le pekage nessessaire
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# pour afficher la page grande
driver.maximize_window()
# on va copier le lien de site de l application qui on veut tester
driver.get("https://espacepourlavie.ca/biodome")
driver.find_element(By.LINK_TEXT,"Je m'abonne à l'infolettre").click()
time.sleep(3)
#driver.find_element(By.CLASS_NAME, "hl-full-bleed-banner__wrapper").is_displayed()

time.sleep(3)
driver.quit()