# on va connecter et ouvrire l application
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# instantiation de l'objet Chrome et on le stock dans la variable "driver"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)
driver.get("https://testautomationpractice.blogspot.com/")
# ------
# #1 afficher le nombre des ligues et des colennes dans la table
# on va selectinner  loacliser la table avec les ligues
# //tagname[@attribute='value']
liste_lignes =driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")

# on va comparer le nombre_lignes_Attendues et nbr_lignes_actuelles
nombre_lignes_Attendues=7
nbr_lignes_actuelles=len(liste_lignes)
assert nbr_lignes_actuelles==nombre_lignes_Attendues ,"le nombre de lignes obtenu est different de celui attandu"
#--------------------
# #afficher le nombre des colonnes
liste_colonnes =driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
nombre_colonnes_Attendues=4
nbr_colonnes_actuelles=len(liste_colonnes)
assert nbr_colonnes_actuelles==nombre_colonnes_Attendues ,"le nombre de colonne obtenu est different de celui attandu"
print("le nombre de ligne actuelle est :", nbr_lignes_actuelles)
print("le nombre de colonnes actuelle est :", nbr_colonnes_actuelles)
# --------------------
# #2lire les donnees d une cellule ou d une colonnes specifique
# inspect une cellule et ecrire le Xpath
contenu_cellule=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[3]").text
print("afficher",contenu_cellule)
assert contenu_cellule=="Selenium","le contenus sont different"
#------------
# #3Lire toutes les données des lignes ou des colonnes
for ligne in range(2,nbr_lignes_actuelles+1):
     for colonne in range(1,len(liste_colonnes)+1):
       data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(ligne) + "]/td[" + str(colonne) + "]").text
       print(data,end="      ")
     print()
#
#
# #4- Lire les données d'une cellule ou d'une si une condition est respectée
#
time.sleep(4)
driver.quit()