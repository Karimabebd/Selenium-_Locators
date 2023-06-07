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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
#il faut donner un peut tempt pour l affichage
time.sleep(2)
#verifier avec rabah
#driver.find_element(By.CLASS_NAME, "oxd-input--active").send_keys("Admin")
#driver.find_element(By.CLASS_NAME, "oxd-input ").send_keys("admin123")
#driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module").is_displayed()
time.sleep(5)
driver.close()