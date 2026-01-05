from selenium.webdriver.common.by import By

class Search: 
      def __init__(self, driver):
         self.driver = driver
      
      def open_amzon(self):
         self.driver.get("https://www.amazon.com/")   
      
      def enter_search_item(self, item):
         self.driver.find_element(By.ID,"twotabsearchtextbox").send_keys(item)   
         self.driver.find_element(By.ID,"nav-search-submit-button").click()
   