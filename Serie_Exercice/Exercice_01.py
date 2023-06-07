#1-	Se connecter sur le site : https://opensource-demo.orangehrmlive.com
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

driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(4)
#3-	Cliquer sur le menu Admin.
driver.find_element(By.CLASS_NAME,"oxd-main-menu-item--name").click()
time.sleep(4)
#4-	Sélectionner users : Admin  user management users.
#driver.find_element(By.CLASS_NAME,"oxd-topbar-body-nav-tab-item").click()

driver.find_element(By.CLASS_NAME,"oxd-topbar-body-nav-tab-item").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-topbar-body-nav-tab-link").click()
time.sleep(4)
#5-	Afficher le nombre total de ligne dans la table des users.
liste_lignes =driver.find_elements(By.XPATH,"//div[@class='oxd-table']/div/div")
liste_lignes==len(liste_lignes)
nbr_lignes_actuelles=len(liste_lignes)

print(nbr_lignes_actuelles)
#
#driver.find_element(By.CLASS_NAME,"oxd-table").text
#orangehrm-container
# driver.find_element(By.CLASS_NAME,"orangehrm-container").text
# #Afficher le nombre total des colonnes  dans la table des users.
liste_colonne =driver.find_elements(By.XPATH,"//div[@class='oxd-table-header']/div/div")
liste_colonne==len(liste_colonne)
nbr_colonne_actuelles=len(liste_colonne)
print(nbr_colonne_actuelles)

# 6-Afficher le nombre total des users (utilisateurs) qui ont un statut : enabled
#7-	Afficher le nombre total des users(utilisateurs)  qui ont un statut : disabled.
enabled_users = 0
disabled_users = 0

for i in range(1,len(liste_lignes)+1):
    # Trouver toutes les cellules dans cette ligne
    cell = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[" + str(i) + "]/div[1]/div[5]").text
    if cell =="Enabled":
        enabled_users =enabled_users +1
    elif cell == "Disabled":
        disabled_users=disabled_users+1

print("Le nombre total d'utilisateurs avec un statut 'enabled' est : ", enabled_users)
print("Le nombre total d'utilisateurs avec un statut 'disabled' est : ", disabled_users)


time.sleep(3)
driver.quit()