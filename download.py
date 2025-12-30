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
driver .get("https://the-internet.herokuapp.com/download")

download_link = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "some-file.txt"))
)
download_link.click()
time.sleep(2)
driver.quit()