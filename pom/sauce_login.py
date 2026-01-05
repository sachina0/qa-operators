from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from sauce import Login

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

login_page = Login(driver)
login_page.open_saucedemo()()
time.sleep(2)
login_page.enter_username("standard_user")
time.sleep(2)
login_page.enter_password("secret_sauce")
time.sleep(2)
login_page.click_login()
time.sleep(2)
assert "inventory" in driver.current_url.lower()
print("sauce demo login test passed")
driver.quit()


