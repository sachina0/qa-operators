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
driver .get("https://the-internet.herokuapp.com/dropdown")

dropdown= Select(driver.find_element(By.ID,"dropdown"))
time.sleep(2)
dropdown.select_by_visible_text("Option 1")
time.sleep(2)
driver.quit()