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
driver.get("https://espacepourlavie.ca/tableau-des-ordres-dinsectes")
time.sleep(3)
#on connecter au 2 eme page on va localise par link
# driver.find_element(By.LINK_TEXT, "Je m'abonne à l'infolettre").click()
# --------------erreur# #on va recupere le titre de la 1 er page (parent) et URL sur la console
# login_URL=driver.current_url
# Title_Attendu=driver.title
# print(login_URL,"",Title_Attendu)
# #pour verifier que les resultat de la 1 er page (parent) est corect
# URL_Attandu="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# Title_Attendu="OrangeHRM"
# assert URL_Attandu == login_URL
# assert Title_Attendu==Title_Attendu
time.sleep(3)
driver.quit()