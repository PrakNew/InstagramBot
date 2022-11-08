from main.HomePage import Login
from selenium import webdriver
from main.ProfileInteraction import ProfileInteraction
import time
from main.ProfileData import ProfileData


driver =  webdriver.Chrome("C:/Users/Anant Singh/Downloads/chromedriver_win32 (1)/chromedriver.exe")

bot= Login(driver)
botActions = ProfileInteraction(driver)
getTopPages = ProfileData(driver)

bot.sign_in()
bot.print_all_handles("food") #prints search results
botActions.follow_unfollow("sodelhi") #follow and unfollow a user(arg=pagename)
botActions.like_unlike("dilsefoodie", 30) #like and unlike n pics of given handle(arg1=pagename, agr2=number of pics to be liked)
botActions.find_followers("sodelhi", 10)
botActions.find_followers("foodtalkindia", 10) #print top n followers of given handle(arg1=pagename, arg2=number of followers to be printed)
botActions.mutual_followers("foodtalkindia") #print mutual followers of given handle(arg=pagename)
botActions.view_story("automation_community_india") #see the story of given handle(arg=pagename)

topPagesSearch=getTopPages.get_top_pages_from_search("food",10,5) #top pages from search results (arg1=handlename, arg2=total number of pages, arg3= pages to be sorted)
getTopPages.number_of_post_count(topPagesSearch) #counts number of posts in last 3 days
totalhashtags=getTopPages.scrape_content(5,topPagesSearch) #gets the caption of n number of posts from top pages(arg = number of posts to be scraped)
frequency=getTopPages.frequency_of_words(totalhashtags) #gets frequency of hashtags present in the scraped content
getTopPages.create_csv_file(frequency) #writes the hashtag frequency in the csv file
getTopPages.most_popular_hashtags(frequency) #return top 5 hashtags and their frequency
getTopPages.plot_pie_chart(frequency) #plots pie chart for hashtags and frequency
likes=getTopPages.get_likes_of_toppages(10,topPagesSearch) #get the like count of top searched pages(arg = number of posts)
average_likes=getTopPages.average_likes(likes) #counts average likes for each page
ratiolist=getTopPages.average_like_vs_followers_ratio(topPagesSearch, average_likes) #calculates the ratio of like vs followers for each page
getTopPages.plot_bar_graph(topPagesSearch,ratiolist) #plot the bar graph for the ratio



time.sleep(20)
driver.quit()