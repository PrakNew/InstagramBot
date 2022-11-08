from bs4 import BeautifulSoup
from main.HomePage import Login
import time
from xpaths import xpaths
from main.wrapper import Wrapper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProfileInteraction():
    
    def __init__(self,driver):
        self.wrapperHelp = Wrapper()
        self.driver=driver
        
    def follow_unfollow(self,pagename):
        Login.open_page(self, pagename)
        time.sleep(2)
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.followUnfollowText)
                
        if self.driver.find_element_by_xpath(xpaths.followUnfollowText).text == 'Follow':
            
            self.wrapperHelp.click(self.driver, By.CSS_SELECTOR, xpaths.followButton)
            print("Followed "+pagename)
        else:
            print("Already Following")
        time.sleep(2)    
        
        if self.driver.find_element_by_xpath(xpaths.followUnfollowText).text == 'Message':
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.unfollowButton)
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.unfollowDialogBpx)
            print("Unfollowed "+pagename)
        else:
            print("Already unfollowed")
                
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.homeButton)
    
    def like_unlike(self,pagename,numberOfPosts):
        Login.open_page(self, pagename)
        time.sleep(2)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.firstPicture)
        
        for j in range(0,numberOfPosts):
            print(j+1)
            self.wrapperHelp.wait_to_appear(self.driver,By.XPATH, xpaths.picDialogBox)
            if BeautifulSoup(self.driver.find_element_by_xpath(xpaths.likeButtonText).get_attribute('outerHTML'),'html.parser').svg['aria-label'] == 'Like':
                self.wrapperHelp.click(self.driver, By.XPATH, xpaths.LikeUnlikeButton)
                print("Liked")
            else:
                print("Already liked")
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.nextPicButton)
            j+=1
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.LikeUnlikeButton)
        
            
        for i in range(0,numberOfPosts):
            print(i+1)
            self.wrapperHelp.wait_to_appear(self.driver,By.XPATH, xpaths.picDialogBox)
            if BeautifulSoup(self.driver.find_element_by_xpath(xpaths.likeButtonText).get_attribute('outerHTML'),'html.parser').svg['aria-label'] == 'Unlike':
                self.wrapperHelp.click(self.driver, By.XPATH, xpaths.LikeUnlikeButton)
                print("Unliked")
            else:
                print("Already unliked")
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.previousPicButton)
            i+=1
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.LikeUnlikeButton)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.closePicButton)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.homeButton)
        
        
    def scroll_follower_panel(self,no_of_followers):
        
        followers_panel = self.driver.find_element_by_xpath(xpaths.followersPanel)
    
        current_scroll_position, new_height= 0, 1
        i = 0
        while i < no_of_followers:
            try:
                follower = self.driver.find_elements_by_xpath(xpaths.follower)[i]
                print(i+1)
                print(BeautifulSoup(follower.get_attribute("innerHTML"),'html.parser').find_all('a',{"class":['FPmhX', 'notranslate'  '_0imsa' ]})[0].text)
                i = i + 1
            except IndexError:
                speed = 0.5
                current_scroll_position = new_height
                new_height = self.driver.execute_script("return arguments[0].scrollHeight",followers_panel)
                while current_scroll_position <= new_height:
                    current_scroll_position += speed
                    self.driver.execute_script("arguments[0].scrollTo(0, arguments[1]);",followers_panel,current_scroll_position)
                time.sleep(2)
            
    def find_followers(self,pagename,no_of_followers):
        Login.open_page(self, pagename)
    
        self.driver.implicitly_wait(10)
        
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.openFollowers)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.openFollowers)
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.followersPanel )
        
        print("Followers of ",pagename,"are : ")
        
        ProfileInteraction.scroll_follower_panel(self, no_of_followers)
           
    def mutual_followers(self,pagename):
        
        Login.open_page(self, pagename)
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.mutualFollowersButton)
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.mutualFollowersButton)
        time.sleep(3)
        mutual_followers_panel = self.driver.find_element_by_xpath(xpaths.mutualFollowersPanel)
    
        current_scroll_position, new_height= 0, 1
        i = 0
        x=self.driver.find_element_by_xpath(xpaths.totalMutualFollowers)
        y=len(x.find_elements_by_tag_name("li"))
        print(y)
        
        while i < y:
            try:
                follower = self.driver.find_elements_by_xpath(xpaths.mutualFollowers)[i]
                print(i+1)
                print(BeautifulSoup(follower.get_attribute("innerHTML"),'html.parser').find_all('a',{"class":['FPmhX', 'notranslate'  '_0imsa' ]})[0].text)
                i = i + 1
            except IndexError:
                speed = 0.5
                current_scroll_position = new_height
                new_height = self.driver.execute_script("return arguments[0].scrollHeight",mutual_followers_panel)
                while current_scroll_position <= new_height:
                    current_scroll_position += speed
                    self.driver.execute_script("arguments[0].scrollTo(0, arguments[1]);",mutual_followers_panel,current_scroll_position)
                time.sleep(2)
    
    def view_story(self, pagename):
        Login.open_page(self, pagename)
        time.sleep(3)
        
        Height = BeautifulSoup(self.driver.find_element_by_xpath(xpaths.storyButtonDimensions).get_attribute("outerHTML"),'html.parser').canvas['height']
        Width = BeautifulSoup(self.driver.find_element_by_xpath(xpaths.storyButtonDimensions).get_attribute("outerHTML"),'html.parser').canvas['width']

        if int(Height) == 208 and int(Width) == 208:
            print("Viewed")
        if int(Height) == 210 and int(Width) == 210:
            
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.storyButton)
            time.sleep(2)
            try :
                self.driver.find_element_by_xpath(xpaths.storyDialogBox)
                self.wrapperHelp.wait_to_disappear(self.driver, By.XPATH, xpaths.storyDialogBox)
            except NoSuchElementException:
                print("No story")
        self.wrapperHelp.click(self.driver, By.XPATH, xpaths.homeButton)
        
        
        
        
            
        