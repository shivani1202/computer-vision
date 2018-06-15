import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
'# -- coding utf-8 --'
def calctime(a):
    return time.time()-a
positive =0
negative =0
compound =0
initime = time.time()
count = 0
plt.ion()
import test
ckey='	PcexmhayidF5JXV3HJJKfK6MY'
csecret='	yj5Wx6SNmTfWDmaKe1vYJ5RmKzjyzkWDOZV5Ib0rjp32v8riKw'
atoken='	900047059289423872-qLoFxNJujdOLCEyWsJdLl0CiGdjboHa'
asecret='	9ZzVliX0yyDWK2dWtvWRbsQIC5PWq5Gv1fyQNJ3cMPqRQ'
class listener(StreamListener):
    
    def on_data(self,data):
        global initime
        
        t = int(calctime(initime))
        
        all_data = json.loads(data)
        tweet = all_data["text"]
        tweet = " ".join(re.findall("[a-zA-z]+",tweet))
        blob = TextBlob(tweet.strip())
        
        global positive 
        global negative
        global compound
        global count
        
        count = count + 1
        senti =0
        
        for sen in blob.sentences:
            senti = senti + sen.sentiment.polarity
            if sen.sentiment.polarity >=0:
                positive = positive +sen.sentiment.polarity
            else:
                negative = negative +sen.sentiment.polarity
            compound = compoud + senti
            
        print(count)
        print(tweet.strip())
        print(senti)
        print(t)
        print(str(positive)+' '+str(negative)+' '+str(compound))
        
        plt.axis([0,70,-20,20])
        plt.xlabel('Sentiment')
        plt.plot([t],[positive],'go',[t],[negative],'no',[t],[compound],'bo')
        plt.show()
        plt.pause(0.0001)
        if count == 200:
            return False
        else:
            return True
    
    def on_error(self,status):
        print(status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

searchTerm = input("Enter keyword/tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

twitterStream = Stream(auth,listener(NoOfTerms))
twitterStream.filter(track = [searchTerm])