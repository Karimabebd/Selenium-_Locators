import time
#on va importer le pekage nessessaire
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#---------- pour afficher la page grande
driver.maximize_window()
# on va copier le lien de site de l application qui on veut tester
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
#afficher le titre
print(driver.title)
#afficher URL
print(driver.current_url)
#driver.get("https://pypi.org/project/webdriver-manager/")
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

# driver.find_element(By.NAME,"Password").click()

# driver.find_element(By.CLASS_NAME,"login-button").click()

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='oxd-topbar-header-title']").is_displayed()
# on va recupere la valeur de message d erreur dans le code

time.sleep(3)

driver.quit()