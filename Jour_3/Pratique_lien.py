#1-	Se connecter sur le site : https://leafletjs.com/reference.html
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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
#2-	Login  avec les identifiants suivants : Admin, admin123.
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.CLASS_NAME,"oxd-input--active").send_keys("admin123")
time.sleep(4)
# pour allez un autre site
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
#pour allez un autre site on modifier un peut le link_text
# driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM").click()
attributDuLie=driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click().get_attribute("href")
print(attributDuLie)
time.sleep(3)
driver.close()