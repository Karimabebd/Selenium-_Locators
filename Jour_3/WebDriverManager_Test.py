#import les package
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#les premiere ligue a faire pour specifier pour PCharme ou ce trouve le driver
#1  pour le code  ou ce trouve le driver
#service_obj = Service("C:\\Selenium\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.selenium.dev/documentation/overview/components/")
# driver.maximize_window()
# time.sleep(5)
# driver.close()
#creer moi un objet vide  de type chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#pour recupere le cite
driver.get("https://www.selenium.dev/documentation/overview/components/")
time.sleep(5)
driver.close()