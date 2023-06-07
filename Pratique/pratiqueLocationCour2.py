import time
#pour connecter sur la page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#utilise chromeDriverManger().install pour installer et gere le pilote chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#pour ouvrir un URL d une page
#driver.get("https://bdeb.omnivox.ca/Login/Account/Login?isLogout=1")
driver.get("https://demo.nopcommerce.com/login?returnurl=%2F")
#on va trouver le champ par sont ID
#localisation par ID pour email
driver.find_element(By.ID, "Email").send_keys("benhaddad@ff")
#driver.find_element(By.ID, "Identifiant").send_keys("2224671")
driver.find_element(By.ID, "Password").send_keys("ANIS2008")
#localisation par classe pour le button login(connecter)

driver.find_element(By.CLASS_NAME, "login-button").click()
#localisation par ID pour password
#driver.find_element(By.ID, "Password").click()

# on va examiner le message d erreur que sa afficher
#pour voir est ce que le message d erreur est afficher
driver.find_element(By.CLASS_NAME, "validation-summary-errors").is_displayed()
#pour afficher le message erreur sur le console
textError = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
print(textError)
assert textError == """Login was unsuccessful. Please correct the errors and try again.
No customer account found"""

time.sleep(5)
driver.close()