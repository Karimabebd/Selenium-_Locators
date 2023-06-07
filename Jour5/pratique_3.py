# on va connecter et ouvrire l application
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://espacepourlavie.ca/tableau-des-ordres-dinsectes")
time.sleep(3)
# #1 afficher le nombre des ligues et des colennes dans la table
# on va selectinner  loacliser la table avec les ligues
# //tagname[@attribute='value']
driver.find_element(By.CLASS_NAME,"tab-donnees")
#pour localiser les ligues
liste_lignes=driver.find_elements(By.XPATH , "//table[@class='tab-donnees']/tbody/tr")
#afficher nombre des ligues
nbr_lignes_actuelles=len(liste_lignes)
print(nbr_lignes_actuelles)

#-----------------------
#1 afficher le nombre  des colennes dans la table
# on va selectinner  loacliser la table avec les colonnes
# //tagname[@attribute='value']
liste_colonnes=driver.find_elements(By.XPATH , "//table[@class='tab-donnees']/tbody/tr[1]/th")
nbr_colonnes_actuelles=len(liste_colonnes)
print(nbr_colonnes_actuelles)
nbr_lignes_attendu=31
nbr_colonnes_attendu=5
assert nbr_lignes_attendu==nbr_lignes_actuelles
assert nbr_colonnes_attendu==nbr_colonnes_actuelles


driver.quit()