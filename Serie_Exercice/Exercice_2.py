

import requests
#1-	Se connecter sur le site : http://deadlinkcity.com/
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
driver.get("http://deadlinkcity.com/")
time.sleep(4)
lien_brisé = []


def get_broken_links():
    # Récupère tous les éléments 'a' (liens) sur la page
    liens = driver.find_elements(By.TAG_NAME, 'a')

    try:
        for lien in liens:
            # Récupère l'URL du lien
            url = lien.get_attribute('href')

            # Envoie une requête GET à l'URL pour vérifier si le lien fonctionne
            response = requests.get(url)

            # Si le code de statut de la réponse est un succès (2xx), passe au lien suivant,
            # sinon, ajoute le lien à la liste des liens brisés
            if response:
                continue
            else:
                lien_brisé.append(url)
    except requests.exceptions.ConnectionError:
        # Si une exception de connexion est levée, imprime l'URL qui l'a causée
        print("Cet URL génère une exception:", url)


# Appelle la fonction qui récupère les liens brisés
get_broken_links()

# Affiche tous les liens brisés trouvés
print("La liste des liens brisés :")
for lien in lien_brisé:
    print(lien)
driver.quit()

