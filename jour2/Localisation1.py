import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
# 1 on va copier le lien de page web
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
# 2 on va inspecter le usename -----//input[@name='username']

driver.find_element(By.NAME,"username").send_keys("Admin")
# 3 on va inspecter le password
driver.find_element(By.NAME, "password").send_keys("admin123")
# 4 on va inspecter le login
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(4)
#afficher que la page est afficher
#driver.find_element(By.CLASS_NAME,"oxd-topbar-header-breadcrumb-module").is_displayed()
time.sleep(4)
driver.quit()
# on va verifier est ce que cette page afficher
#
