#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#https://www.orangehrm.com/
#1 copier le code pour conneter au page
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# https://www.orangehrm.com/
# instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#-----------------------------------------
#recuperer URL (script,manuellement) de la 1 er page (parent)
login_URL = driver.current_url  #script
URL_Attendu="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"   #manuellement
#la comparaission entre les deux resultat(script, #manuellement) de la 1 er page (parent)
assert login_URL== URL_Attendu ,"le titre de la page ne correspond pas au titre atendu"
#----------------------------------------
#recuperer Titre de la page (script,manuellement) de la 1 er page (parent)
Titre_ATTENDU="OrangeHRM"  #manuellement
login_title = driver.title  #script
#la comparaission entre les deux resultat(script, #manuellement)
assert login_title==Titre_ATTENDU ,"Le titre de la page ne correspond pas au titre attendu"
#--------------------------------------
#afficher le titre et URL
print(login_title,login_URL )
#-------------------

#pour la 2 eme page on peut commecter a la 2 eme page (driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click())
#partir a autre page 2 on va recuper ID
ID_parent = driver.current_window_handle
print(ID_parent)
time.sleep(6)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
#Pour afficher la liste ID (tout les page ouverte) page parent et suite--
IDs = driver.window_handles
ID_login = IDs [0]
ID_home = IDs [1]
print(ID_login,"****",ID_home)
#Pour aller a la page 2
driver.switch_to.window(ID_home)
# pour faire la comparaision
home_URL = driver.current_url
home_Attendu="https://www.orangehrm.com/"
assert home_URL== home_Attendu ,"le titre de la page ne correspond pas au titre aatendu"
#---------------------------
#pour retourner a la page 1
driver.switch_to.window(ID_login)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("Admin123")

time.sleep(4)
driver.quit()
