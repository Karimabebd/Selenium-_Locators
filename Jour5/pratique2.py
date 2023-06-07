#accer au page wobe
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://espacepourlavie.ca/tableau-des-ordres-dinsectes")
time.sleep(4)
#1 afficher le nombre des ligues  dans la table
Liste_lignes = driver.find_elements(By.XPATH, "//table[@class='tab-donnees']/tbody/tr")
valeur_attendu=31
valeur_actuelle=len(Liste_lignes)
assert valeur_actuelle == valeur_attendu
# #afficher les colennes dans la table
Liste_colonne = driver.find_elements(By.XPATH, "//table[@class='tab-donnees']/tbody/tr[1]/th")
valeur_attendu_colonnes=5
valeur_actuelle_colonnes=len(Liste_colonne)
assert valeur_actuelle_colonnes == valeur_attendu_colonnes
#afficher le nombredes ligne et nombre des colones
print(valeur_actuelle, "****",valeur_actuelle_colonnes)
#---------------------------------------------------------
#2lire les donnees d une cellule ou d une colonnes specifique

contenu_cellule = driver.find_element(By.XPATH, "//table[@class='tab-donnees']/tbody/tr[2]/td[3]").text
assert contenu_cellule =="Absentes"
print("le contenu de la cellule est:",contenu_cellule )
contenu_cellule = driver.find_element(By.XPATH, "//table[@class='tab-donnees']/tbody/tr[2]/td[5]").text
assert contenu_cellule =="Absente"
print("le contenu de la cellule est:",contenu_cellule )
contenu_cellule = driver.find_element(By.XPATH, "//table[@class='tab-donnees']/tbody/tr[4]/td[5]").text
assert contenu_cellule =="Complète"
print("le contenu de la cellule est:",contenu_cellule )
#----------------------------------------
#afficher #3Lire toutes les données des lignes ou des colonnes
for ligne in range(2,len(Liste_lignes)+1):
    for colonne in range(1,len(Liste_colonne)+1):
      data = driver.find_element(By.XPATH,"//table[@name='tab-donnees']/tbody/tr[" + str(ligne) + "]/td[" + str(colonne) + "]").text
      print(data,end="      ")
    print()


time.sleep(4)
driver.quit()