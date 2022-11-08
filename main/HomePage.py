from selenium.webdriver.common.keys import Keys
from xpaths import xpaths
from main.wrapper import Wrapper
from selenium.webdriver.common.by import By
from jproperties import Properties

class Login():
    def __init__(self,driver):
        
        self.wrapperHelp = Wrapper()
        self.driver = driver
       
    def sign_in(self):
        
        self.driver.get("https://www.instagram.com/?hl=en")
        self.driver.maximize_window()
        configs = Properties()
        with open('C:/Users/Anant Singh/eclipse-workspace/InstagramBot/credentials.properties','rb') as config_file:
            configs.load(config_file)
    
        self.wrapperHelp.sendKeys(self.driver, By.XPATH,xpaths.usernameInput,configs.get("username").data)
        self.wrapperHelp.sendKeys(self.driver, By.XPATH, xpaths.passwordInput,configs.get("password").data)
       
        self.wrapperHelp.sendKeys(self.driver, By.XPATH, xpaths.passwordInput ,Keys.ENTER)
        
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.notNow1)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.notNow2)
        
    def print_all_handles(self,pagename):
        
        self.wrapperHelp.sendKeys(self.driver, By.XPATH, xpaths.SearchBar, pagename)
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.SearchResultsDialogBox)
        x = self.driver.find_element_by_xpath(xpaths.SearchResultsDialogBox)
        y = x.find_elements_by_tag_name("a")
        for i in y:
            searchResults = str(i.find_element_by_class_name(xpaths.searchResultsHeader).text)
            if(not searchResults.startswith("#")):
                print(searchResults)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.searchBarClear)
                
    def open_page(self,pagename):

        self.wrapperHelp.sendKeys(self.driver, By.XPATH, xpaths.SearchBar, pagename)
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.SearchResultsDialogBox)
        self.wrapperHelp.sendKeys(self.driver, By.XPATH, xpaths.SearchBar, Keys.DOWN)
        self.wrapperHelp.sendKeys(self.driver, By.XPATH, xpaths.SearchBar, Keys.ENTER)
        

        