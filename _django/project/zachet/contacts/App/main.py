# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:52:03 2018

twitter rumors_analisation
@author: Alexandr
"""


import twitter
import io, json
from .utils import DataAnalyse
from .utils import UserAnalyse
from .utils import UserData
from .utils import TextAnalyse

def twtt(search_text,lang,count,from_data,To):
    api = twitter.Api(consumer_key='nHJk2wTXRlew6WfozdV9JPqVk',
        consumer_secret='RBzO3UDCWUf2XvN4lR1WOBbG4233sCXSrit0DnzTDSKeXkfq3v',
        access_token_key = 	"296713992-Wg6eClZnnTHW7gimaDDBgNYsI2aXR2augsUV63OS",
        access_token_secret=	"e04ALSkMR9ylO8C5JRyQqkP7V4m3T2EIQR2SoWiftGnw3")

    q = "q="+str(search_text)
    lng = lang
    cnt = "count="+str(count)
    qr = q+"&"+lng+"&"+cnt
    for tweet in api.GetSearch(raw_query=qr):
  #      with io.open('data/tweet.json', 'w', encoding='utf-8') as f:
  #          f.write(json.dumps(tweet._json, ensure_ascii=False))
        
        regYears = UserData.registration_years(tweet)
        
        credibility = UserAnalyse.Credibility(UserData.user_verified(tweet))
        
        role = UserAnalyse.Role(UserData.followers_count(tweet),UserData.friends_count(tweet))
        
        inf = UserAnalyse.Influence(UserData.statuses_count(tweet))

        retweets = (UserData.retweet_count(tweet,api))
        
        replies = (UserData.statuses_count(tweet))
        
        engagement = UserAnalyse.Engagement(tweet.user.statuses_count,retweets,tweet.user.favourites_count,replies,regYears)
        
        originallity = UserAnalyse.Originallity(tweet.user.statuses_count,UserData.retweet_count(tweet,api))

        timeline = api.GetUserTimeline(tweet.user.id, count=1) 
#      with io.open('data/timeline.json', 'w', encoding='utf-8') as f:
   #         f.write(json.dumps(tweet._json, ensure_ascii=False))
        
        hashtags = DataAnalyse.Hashtags(timeline[0])
        
##        Abr_Find = DataAnalyse.Abr_Find(timeline[0].text)
        
 #       Vulgar_Find = DataAnalyse.Vulgar_Find(timeline[0].text)
        
  #      Mean_Find = DataAnalyse.Mean_Find(timeline[0].text)
        
 #       Emoji_Find = DataAnalyse.Emoji_Find(timeline[0].text)
        
        retweet_count = DataAnalyse.retweet_count(timeline[0])
        
        favorite_count = DataAnalyse.favorite_count(timeline[0])
        
        Word_Count = TextAnalyse.Word_Count(timeline[0].text)
        
        slogi = TextAnalyse.slogi(timeline[0].text,lang)