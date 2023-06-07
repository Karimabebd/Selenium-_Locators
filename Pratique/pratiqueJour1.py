import time
#pour connecter sur la page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#por naviger
driver.get("https://codepen.io/pen/")
#driver.get("https://consulatalgeriemontreal.com/v1.0/")
#pour mettre la page au max
driver.maximize_window()
#pour donner une duree de  5s attand
time.sleep(5)
#pour afficher le titre de la page
print(driver.title)
#pour afficher le URL
print(driver.current_url)
#pour afficher la page
print(driver.page_source)
#on va connecter sur consulat apres on va alles au college boisb# (consolat--->bdeb)
driver.get("https://www.bdeb.qc.ca/")
#il va retourner ver consulat  #(bdeb--->consulat)
driver.back()
time.sleep(6)
#pour retournner  au cite ddu consulat
driver.forward()   # retourne arrierr marcherier

driver.close()