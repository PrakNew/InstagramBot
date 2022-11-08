'''
Created on 7 Sep, 2020

@author: Anant Singh
'''
import time
from bs4 import BeautifulSoup
from main.wrapper import Wrapper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from xpaths import xpaths
import re
from main.HomePage import Login
import csv
import matplotlib.pyplot as plt
from main.utility import Utility


class ProfileData():
    
    def __init__(self,driver):
        
        self.driver = driver
        self.wrapperHelp = Wrapper()
        self.utilityHelp = Utility()
        
    def get_top_pages_from_search(self,pagename,fromPages,numberOfPages):
        
        toppages = []
        totalFollowers = []
        self.wrapperHelp.sendKeys(self.driver, By.XPATH,xpaths.SearchBar, pagename)
        
        self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.SearchResultsDialogBox)
        x = self.driver.find_element_by_xpath(xpaths.SearchResultsDialogBox)
        y = x.find_elements_by_tag_name("a")
        for i in y:
            z = str(i.find_element_by_class_name(xpaths.searchResultsHeader).text)
            if(not z.startswith("#")):
                toppages.append(z)
        del toppages[fromPages:]
         
        for j in range(0,fromPages):
            self.driver.get('https://www.instagram.com/' +toppages[j]+ '/')
            self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.followersCount)
            numberOfFollowers1 = BeautifulSoup(self.driver.find_element_by_xpath(xpaths.followersCount).get_attribute("outerHTML"),'html.parser').span['title']
            numberOfFollowers = (numberOfFollowers1.replace(',',''))
            totalFollowers.append(numberOfFollowers)    
             
            j+=1
    
        topPagesSearch=self.utilityHelp.merge_two_lists(totalFollowers, toppages, numberOfPages)
        print(topPagesSearch)
        return topPagesSearch
        
            
    def number_of_post_count(self,topPagesSearch):
        
        for i in topPagesSearch:
            Login.open_page(self,i)
            time.sleep(2)
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.firstPicture)
            time.sleep(2)
            count=0
            for j in range(0,50):
                self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.postTime)
                datevalue= self.driver.find_element_by_xpath(xpaths.postTime)
                
                val=str(datevalue.text)
                if val=="4 DAYS AGO":
                    time.sleep(3)
                    break
                    
                else:
                    self.wrapperHelp.click(self.driver, By.XPATH, xpaths.nextPicButton)
                    count+=1
                j+=1
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.closePicButton)
            print(i)
            print(count)
            
            
    def scrape_content(self, numberOfPosts,topPagesSearch):
        
        top_5_post_content={}
        totalhashtags=[]
        
        for i in topPagesSearch:
            Login.open_page(self, i)
            time.sleep(2)
            self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.firstPicture)
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.firstPicture)
            post_content={}
            
            for j in range(0,numberOfPosts):
                time.sleep(2)
                num='post'+str(j+1)
                self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.captionContent)
                data=self.driver.find_element_by_xpath(xpaths.captionContent)
                value=data.text
                hashtags = re.findall(r'#\w+', value)
                if hashtags is not None:
                    
                    totalhashtags.append(hashtags)
                
                post_content[num]=(value.encode('utf-8'))
                self.wrapperHelp.click(self.driver, By.XPATH, xpaths.nextPicButton)
                j+=1
            
            top_5_post_content[i]=post_content
            self.wrapperHelp.sendKeys(self.driver, By.XPATH,xpaths.nextPicButton , Keys.ESCAPE)
            time.sleep(2)
        
        print(top_5_post_content)
        return totalhashtags

    def frequency_of_words(self,totalhashtags):

        hashtags = [x for x in totalhashtags if x]
        singlehashtags = self.utilityHelp.sublist_into_list(hashtags)

        frequency=self.utilityHelp.count_of_list_items(singlehashtags)
        print(frequency)
        return frequency
        
    def create_csv_file(self,frequency):
    
        with open('data.csv','w',newline="") as f:
            w = csv.writer(f)
            writer = csv.DictWriter(f, fieldnames=["Hashtags", "count"])
            writer.writeheader()
            w.writerows(frequency.items())
        
    def most_popular_hashtags(self,frequency):
        
        top_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        top_freq=top_freq[:5]
        for i in top_freq:
            print(i[0], i[1])
            
    def plot_pie_chart(self,frequency):
        
        new_total_words_with_freq=sorted(frequency,key=frequency.get,reverse=True)

        top_5_hash=[]
        top_5_times=[]
        for i in range(5):
            top_5_hash.append(new_total_words_with_freq[i])
            top_5_times.append(frequency[new_total_words_with_freq[i]])

        plt.pie(top_5_times,labels=top_5_hash,autopct="%.2f%%")
        plt.show()
        plt.savefig('piechart.png')
        plt.close('all')
        
    def get_likes_of_toppages(self,numberOfPosts,topPagesSearch):
        
        likes={}

        for i in topPagesSearch:
            Login.open_page(self, i)
            time.sleep(2)
            self.wrapperHelp.wait_to_appear(self.driver, By.XPATH, xpaths.firstPicture)
            self.wrapperHelp.click(self.driver, By.XPATH, xpaths.firstPicture)
            post_content={}

            for j in range(0,numberOfPosts):
                time.sleep(1)
                num='post'+str(j+1)

                try:
                    time.sleep(1)
                    data = self.driver.find_element_by_xpath(xpaths.countLikes)
                    value = data.text
                    value = value.replace(',','')
                    value = int(value)
                    post_content[num]=value
                    self.wrapperHelp.click(self.driver, By.XPATH ,xpaths.nextPicButton)
                    
                except NoSuchElementException:
                    self.wrapperHelp.click(self.driver, By.XPATH, xpaths.videoViews)
                    time.sleep(1)
                    data = self.driver.find_element_by_css_selector(xpaths.likesInViews)
                    value = data.text
                    value = value.replace(',','')
                    value = int(value)
                    post_content[num]=value
                    self.wrapperHelp.click(self.driver, By.XPATH, xpaths.likesDialog)
                    self.wrapperHelp.click(self.driver, By.XPATH ,xpaths.nextPicButton)
                    
                    
                
            likes[i]=post_content
            self.wrapperHelp.sendKeys(self.driver, By.XPATH,xpaths.nextPicButton , Keys.ESCAPE)
            time.sleep(1)
        
        print(likes)
        return likes
        
    def average_likes(self,likes):
        
        average_likes={}
        for i in likes:
            count=0
            total_sum=0
             
            dic=likes[i]
            for j in dic:
                count=count+1
                total_sum+=dic[j]
                average=total_sum//count
            average_likes[i]=average
        print(average_likes)
        return average_likes
        
    def average_like_vs_followers_ratio(self,topPagesSearch,average_likes):
        
        totalFollowers=[]
        
        for j in range(0,len(topPagesSearch)):
            self.driver.get('https://www.instagram.com/' +topPagesSearch[j]+ '/')
            time.sleep(2)
            numberOfFollowers = BeautifulSoup(self.driver.find_element_by_xpath(xpaths.followersCount).get_attribute("outerHTML"),'html.parser').span['title']
            numberOfFollowers = (numberOfFollowers.replace(',',''))
            totalFollowers.append(numberOfFollowers)    
             
            j+=1
        
        ratiolist = []
        dict={}
        for i in range(0, len(totalFollowers)): 
            totalFollowers[i] = int(totalFollowers[i]) 
        pages= list(average_likes.keys())
        average = list(average_likes.values())
        
        for i in range(0,len(totalFollowers)):
            ratio = average[i]/totalFollowers[i]
            i+=1
            ratiolist.append(ratio)
            
        for i in range(len(totalFollowers)):
            dict[pages[i]]=ratiolist[i]
            
        print(dict)
        return ratiolist
        
    def plot_bar_graph(self,topPagesSearch,ratiolist):
        
        plt.bar(topPagesSearch,ratiolist,color='Red')
        plt.xticks(rotation=90)
        plt.xlabel('Handles')
        plt.ylabel('Like vs Followers ratio')
        plt.title('Handle vs Like Followers Ratio')
        plt.show()
            
    
        
            
            
        
            
        
            
                
        