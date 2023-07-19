#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#https://www.orangehrm.com/
import time

from Tools.scripts.generate_opcode_h import footer
from selenium import webdriver
from selenium.webdriver.common.by import By

# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# https://www.orangehrm.com/
# instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(6)
# footer=driver.find_element(By.CLASS_NAME,"orangehrm-login-footer-sm")
# liste_liens = footer.find_elements(By.TAG_NAME,"a")
# for lien in liste_liens:
#     lien.click()
# ids=driver.window_handles
# for winId in ids:
#     driver.switch_to.window(winId)
#   if driver.title=="OrangeHRM Inc - YouTube":
# time.sleep(4)
# driver.quit()
