
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Wrapper():
           
    def click(self,driver, by, locator):
        
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((by,locator)))
        driver.find_element(by,locator).click()
    
    def sendKeys(self,driver, by,locator, value): 
        
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((by,locator)))
        driver.find_element(by,locator).send_keys(value)
            
    def wait_to_appear(self,driver,by,locator):
        
        try:    
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((by,locator)))
            return True
        except NoSuchElementException:
            return False
    
    def wait_to_disappear(self, driver,by,locator):
        
        try:
            WebDriverWait(driver,30).until_not(EC.presence_of_element_located((by,locator)))
            return True
        except NoSuchElementException:
            return False
            
    
    