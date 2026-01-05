from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from search import Search

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

search_page = Search(driver)

search_page.open_amzon()
time.sleep(2)

search_page.enter_search_item("laptop")
time.sleep(2)

assert"laptop" in driver.current_url.lower()
print("amazon search test passed")
driver.quit()