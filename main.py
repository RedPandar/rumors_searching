# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:52:03 2018

twitter rumors_analisation
@author: Alexandr
"""


import twitter
from time import sleep
import io, json
api = twitter.Api(consumer_key='EzWpyK9RyrOeRpgrefXdvXjrg',
consumer_secret='IdHd4fMbobMujDITJHJ4wpFZ4vlcZxO68r5ofQhrR8l9gUqHGo',
access_token_key = 	"296713992-YdgVZFM3requrT7s5aVMbav8hXonttWLZmvgBWam",
access_token_secret=	"G1zujW6QStwMlbagvSrjf0s46IDsItfvWF5v0O3lZXLUW")
app_name = "Rumors Searching"


for tweet in api.GetSearch(raw_query="q=twitter%20&result_type=text&count=1&lang=ru"):
    with io.open('data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tweet.user._json, ensure_ascii=False))
    print(tweet.user.id)
    timeline = api.GetUserTimeline(tweet.user.id, count=1)
    print(timeline)
#    print(tweet.user.verified)
#    print(tweet.retweet_count)
#    print(tweet.favorite_count)
    sleep(.75)


def Credibility(verified:bool):
    if verified ==True:
     return print("Credibility = 1")
    else:
     return print("Credibility = 0")
     
def Originallity(twt_count:int,retwt_count:int):
    return twt_count/retwt_count

def Influence(Influence:int):
    return Influence

def Role(followers:int,followees):
    return followers/followees

def Engagement(tweets:int,retweets:int,replies:int,favorites:int,acc_age:int):
    return (tweets+retweets+replies+favorites)/(acc_age)