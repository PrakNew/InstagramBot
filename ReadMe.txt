Installations to be done in cmd:

pip install beautifulsoup4  #Beautiful Soup is a Python library for pulling data out of HTML and XML files
pip install jproperties	    #jProperties is a Java Property file parser and writer for Python. It aims to provide the same functionality as Java's Properties class, although currently the XML property format is not supported
pip install matplotlib	    #used for data visualization 

How to run the application:-

1) Enter your username and password in credentials.
2) Change the location of driver in InstagramBot and credentials in sign_in.
3) Run InstagramBot.py

Details of all the files in project structure: -

•	Class HomePage:
o	signIn(): It will take username and password from credentials file and log the user in Instagram.	
o	printAllHandles(): uses search() method then prints all the search results.
o	openPage():uses search() method and opens the given page.

•	Class ProfileInteraction():
o	followUnfollow(): uses openPage() and follows and unfollowes any given user.
o	open_first_pic(): uses openPage() then opens the first pic of that profile.
o	like_pic(): uses open_first_pic() then likes that picture.
o	unlike_pic(): uses open_first_pic() then unlikes that picture.
o	like_unlike_top_pics(): takes input from the user to like or unlike any given number of pictures.
o	scrollFollowersPanel(): uses openFollowers() and scrolls the followers panel.
o	openFollowers(): uses openPage() to open any given profile then opens the followers panel.
o	print_Followers(): uses scrollFollowersPanel() and openFollowers() then prints any number of followers as given by the user.
o	mutual_followers(): uses scrollFollowersPanel() and open Followers() and prints mutual followers between any two given profiles.
o	check_story(): uses openPage() then opens the story of that profile and print message if there is not story.

•	Class ProfileData():
o	getTopFivePages(): uses search() to get search results then openPage() to open profile of 10 top results and sort them in top 5 on the basis of number of followers.
o	getPagesData(): uses openPage() to open the profile of top 5 pages then uses open_first_pic() to the get the number of likes, captions and hashtags. 
o	calculateOperations(): calculates the average number of likes and ratios of followers to likes.
o	plotPieChart(): takes the data from .csv and generates a pie chart of top 5 words.
o	plotBarGraph(): takes the data from .csv and generates a bar graph of the given data.
.





