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

time.sleep(4)
driver.quit()
