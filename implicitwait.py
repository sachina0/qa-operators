from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#setup
sercive = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=sercive)
driver .get("https://www.amazon.com/")

#expliocit wait
driver.implicitly_wait(10)
search = driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("laptop")
button = driver.find_element(By.ID,"nav-search-submit-button")
button.click()
print("implicit wait completed")
driver.quit()