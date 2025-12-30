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
driver .get("https://the-internet.herokuapp.com/checkboxes")
checkbox1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
checkbox2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')      
checkbox1.click()
time.sleep(2)
checkbox2.click()
print("Checkbox 1 clicked: ", checkbox1.is_selected())
print("Checkbox 2 clicked: ", checkbox2.is_selected())
time.sleep(2)
driver.quit()  