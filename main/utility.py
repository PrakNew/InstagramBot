
class Utility():
    
    def merge_two_lists(self,totalFollowers,toppages,numberOfPages):
        
        haveTopFollowers=[]
        if len(toppages)==len(totalFollowers):
            if len(toppages)>=numberOfPages:
                namesTemp = toppages[:]
                followersTemp = list(map(int,totalFollowers[:]))
                    
                for i in range(numberOfPages):
                    ind = followersTemp.index(max(followersTemp))
                    haveTopFollowers.append(namesTemp[ind])
                    namesTemp.pop(ind)
                    followersTemp.pop(ind)                    
            else:
                print("please input the number less than ",len(toppages))
        else:
            print("number of names is not equal to number of followers")
        return haveTopFollowers
    
    def count_of_list_items(self,singlehashtags):
        
        frequency={}
        for i in singlehashtags:           
            if i in frequency:
                frequency[i] = frequency[i]+1
            else:
                frequency[i]=1                
        return frequency
    
    def sublist_into_list(self,hashtags):   
        
        singlehashtags = [item for sublist in hashtags for item in sublist]
        return singlehashtags