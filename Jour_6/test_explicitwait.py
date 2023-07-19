import pytest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#Creation d un objet avec 2 paramettre (driver et temps limite d attente pour selenium)
wait=WebDriverWait(driver,10)
# driver.implicitly_wait(25)
def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # time.sleep(4)
    # driver.find_element(By.NAME,"username").send_keys("Admin")
    #--------attent la presence d element
    username_input= wait.until(ec.presence_of_element_located((By.NAME,"username")))
    username_input.send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    time.sleep(4)
    driver.quit()