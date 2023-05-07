import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# pour afficher la page grande
driver.maximize_window()
# on va copier le lien de site de l application qui on veut tester
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
time.sleep(3)
# pour checher un element par Id(find_element c une methode qui va checher un element par sont ID et Send_keys pour ecrire dans la zone de text
driver.find_element(By.ID, "Email").send_keys("test@test.com")
driver.find_element(By.ID, "Password").send_keys("test1234")
driver.find_element(By.CLASS_NAME, "login-button").click()
# on va examiner le message d erreur que sa afficher
driver.find_element(By.CLASS_NAME, "validation-summary-errors").is_displayed()
# on va recupere la valeur de message d erreur dans le code
textError = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text
print(textError)
# assert "Login was unsuccessful" in textError
time.sleep(5)
driver.close()
# on va verifier
assert textError == """Login was unsuccessful. Please correct the errors and try again.
# No customer account found"""
