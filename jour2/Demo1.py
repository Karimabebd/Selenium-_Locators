import time
#on va inporter le pekage nessessaire
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#---------- pour afficher la page grande
driver.maximize_window()
# on va copier le lien de site de l application qui on veut tester
driver.get("https://www.bdeb.qc.ca/")
time.sleep(3)
#---------------pour afficher le titre de la page 1 methode
print(driver.title)
driver.get("https://pypi.org/prject/webdriver_menager/")
time.sleep(3)
#------pour afficher le titre de la page 2 methode
#titre=driver.title
#print(titre)
#------afficher url sur la console
print(driver.current_url)
#---------afficher le code source
print(driver.page_source)
#-----------por retourne a la page 1 (bois de boulongue)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
#---------pour refresh la page
driver.refresh()
time.sleep(3)
driver.quit()