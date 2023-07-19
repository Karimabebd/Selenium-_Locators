#1- Se connecter au site : https://videotron.com/
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(" https://videotron.com/")
time.sleep(3)
#2- Trouver le nombre d’images sur le site et l’afficher dans la console de votre éditeur de code.
# 3- Afficher la valeur de l’attribut « alt » des images du site dans la console.
images = driver.find_elements(By.TAG_NAME,"img")
print("Nombre d’images sur le site: ", len(images))

# for image in images:
#     print(image.get_attribute('alt'))

for image in images:
    alt_text = image.get_attribute('alt')
    print("Attribut 'alt' de l'image :", alt_text)

#4- Trouver le nombre de liens sur le site et l’afficher dans la console.
liens=driver.find_elements(By.TAG_NAME,"a")
print("Le nombre total de liens sur la page est: ", len (liens))
#5- Trouver le nombre de liens dans la section « footer » du site et l’afficher dans la console.
# 6- Récupérer la valeur de l’attribut « hrf » de chaque lien dans la section « footer » du site et l’afficher dans la console.
footer = driver.find_element(By.TAG_NAME,"footer")
footer_links = footer.find_elements(By.TAG_NAME,"a")
print("Nombre de liens dans le footer: ", len(footer_links ))
for link in footer_links: print(link.get_attribute('href'))
driver.quit()