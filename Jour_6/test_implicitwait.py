import pytest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
###Mecanisme d attente DYNAMIQUE - avec un suil Max d attente\si l element s affiche avant
driver.implicitly_wait(400000)
def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(4)#un mecanisme statique## on va rajouter du tems afin de ralentir selenium pour la chance aux elements pour qu ils soient affiches
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    time.sleep(4)
    driver.quit()