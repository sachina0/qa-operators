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

#promtting alert box
driver .get("https://the-internet.herokuapp.com/javascript_alerts")  
#prompt box
prompt_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
prompt_button.click()
time.sleep(2)
prompt = driver.switch_to.alert
prompt.send_keys("QA Alert")
time.sleep(2)
prompt.accept()
time.sleep(2)
driver.quit()