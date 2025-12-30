from selenium import webdriver

# Open Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Keep browser open for 5 seconds
import time
time.sleep(5)

# Close browser
driver.quit()