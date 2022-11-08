
class xpaths():
    #Login
    usernameInput="//input[@name='username']"
    passwordInput="//input[@name='password']"
    notNow1="//button[contains(text(),'Not Now')]"
    notNow2="//button[contains(text(),'Not Now')]"
    
    #Search Feature
    SearchBar = "//input[@type='text']"
    SearchResultsDialogBox="//div[@class='fuqBx']"
    searchBarClear = "(//nav//div)[10]"
    searchResultsHeader = "Ap253"
    
    #follow_unfollow    
    unfollowButton= "(//button)[2]"
    unfollowDialogBpx = "//button[contains(text(),'Unfollow')]"
    followersPanel = "//div[@class = 'isgrP']"
    followUnfollowText = "(//button)[1]"
    followersPanel = '//div[@class = "isgrP"]'
    follower = "//div[@class = 'PZuss']/li"
    openFollowers = "(//li//a)[1]"
    mutualFollowersButton = "//a[@class='_32eiM']"
    mutualFollowersPanel = "//div[@class = 'isgrP']"
    totalMutualFollowers = "//div[@class = 'PZuss']"
    mutualFollowers = "//div[@class = 'PZuss']/li"
    followersCount = "(//span[@class='g47SY '])[2]"
    followButton="#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button"
    
    # like_unlike
    homeButton = "//img[@alt='Instagram']"
    firstPicture= "(//div[@class='_9AhH0'])[1]"
    LikeUnlikeButton = "(//button[@class='wpO6b '])[3]"
    closePicButton = "//*[local-name()='svg'][@aria-label='Close']"
    picDialogBox = "(//article)[2]"
    likeButtonText = "(//*[local-name()='svg'])[11]"
    nextPicButton = "//a[contains(text(),'Next')]"
    previousPicButton = "//a[contains(text(),'Previous')]"
    
    #Story    
    storyButton="//div[@class = 'XjzKX']/div"    
    storyButtonDimensions = "//canvas[@class='CfWVH']"
    storyDialogBox = "//div[@class='GHEPc']"
    
    #Caption and post likes
    likesDialog = "//div[@class='QhbhU']"
    likesInViews = "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div > div.vJRqr > span"
    videoViews = "//span[@class='vcOH2']"
    countLikes =  "//div[@class='Nm9Fw']//button//span"
    captionContent = '//div[contains(@class,"C4VMK")]/span'
    postTime = "//a[@class='c-Yi7']//time"
    
    