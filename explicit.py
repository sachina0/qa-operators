from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#setup 
sercive = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=sercive)
driver.get("https://www.amazon.com/")
wait = WebDriverWait(driver,10)


#WAIT for search box to be clickable   
search = wait.until(EC.element_to_be_clickable((By.ID,"twotabsearchtextbox")))
search.send_keys("laptop")
#wait for search button to be clickable   
button = wait.until(EC.element_to_be_clickable((By.ID,"nav-search-submit-button")))
button.click() 
# wait for search results
results = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    )
)

# print content of first result
first_result = results[1]
print("----- FIRST RESULT CONTENT -----")
print(first_result.text)

driver.quit()