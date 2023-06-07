#accer au page wobe
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://espacepourlavie.ca/tableau-des-ordres-dinsectes")
time.sleep(5)

# #1 afficher e nombre des ligues et des colennes dans la table
liste_lignes=driver.find_element(By.XPATH,"//table[@class='tab-donnees']/tbody/tr")
# Liste_lignes = driver.find_elements(By.XPATH, "//table[@class='table--plain']/tbody/tr")
# ------------erreur-------------------------------------------------------
# nombre_lignes_Attendues=31
# nbr_lignes_actuelles=len(liste_lignes)
# assert nbr_lignes_actuelles==nombre_lignes_Attendues
# #--------------------------------------------------------------------
# afficher les colennes dans la table
Liste_colennes = driver.find_elements(By.XPATH, "//table[@class='tab-donnees']/tbody/tr[1]/th")
valeur_colennes_attendu=5
valeur_colennes_actuelle=len(Liste_colennes)
assert valeur_colennes_attendu == valeur_colennes_actuelle, "le nombre de colonne  obtenu est different de celui attandu"
# -----------
# #affichage le contenu de la cell
contenu_cellule=driver.find_element(By.XPATH,"//table[@class='tab-donnees']/tbody/tr[3]/td[1]").text
print("afficher",contenu_cellule)
assert contenu_cellule=="Blattoptères","le contenus sont different"

# #3Lire toutes les données des lignes ou des colonnes
for ligne in range(2,len(Liste_lignes)+1):
    for colonne in range(1,len(Liste_colennes)+1):
      data=driver.find_element(By.XPATH,"//table[@name='table--plain']/tbody/tr[" + str(ligne) + "]/td[" + str(colonne) + "]").text
    print(data,end="      ")
    print()

# time.sleep(4)
driver.quit()