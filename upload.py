from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
#setup 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver .get("https://the-internet.herokuapp.com/upload")

file_input = driver.find_element(By.ID, "file-upload")
file_input.send_keys("//Users/sachinamaharjan/Desktop/assignment.docx")  
driver.find_element(By.ID, "file-submit").click()
time.sleep(2)
