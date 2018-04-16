# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:52:03 2018

twitter rumors_analisation
@author: Alexandr
"""


import twitter
import datetime
from time import sleep,ctime
import io, json

api = twitter.Api(consumer_key='EzWpyK9RyrOeRpgrefXdvXjrg',
consumer_secret='IdHd4fMbobMujDITJHJ4wpFZ4vlcZxO68r5ofQhrR8l9gUqHGo',
access_token_key = 	"296713992-YdgVZFM3requrT7s5aVMbav8hXonttWLZmvgBWam",
access_token_secret=	"G1zujW6QStwMlbagvSrjf0s46IDsItfvWF5v0O3lZXLUW")
app_name = "Rumors Searching"

def Credibility(verified:bool):
    if verified ==True:
     return print("Credibility = 1")
    else:
     return print("Credibility = 0")
     
def Originallity(twt_count:int,retwt_count:int):
    return print("Originallity = ",twt_count/retwt_count)

def Influence(Influence:int):
    return print("Influence = ",Influence)

def Role(followers:int,followees):
    return print("Role = ",followers/followees)

def Engagement(tweets:int,retweets:int,replies:int,favorites:int,acc_age:int):
    return print("Engagement = ",(tweets+retweets+replies+favorites)/(acc_age))

for tweet in api.GetSearch(raw_query="q=TheWalkingDead&result_type=text&count=1&src=hash"):
    with io.open('tweet.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tweet._json, ensure_ascii=False))

    print("==============================================================")
    
    timeline = api.GetUserTimeline(tweet.user.id, count=1) 
    with io.open('timeline.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tweet._json, ensure_ascii=False))

    print("Текст Твита: ",timeline)
    print("==============================================================")
    print("Данные пользователя")
    print("Имя пользователя: ",tweet.user.screen_name)
    print("ID пользователя: ",tweet.user.id)
    print("Проверен: ",tweet.user.verified)
    print("Подписан: ",tweet.user.followers_count)
    print("Подписчики: ",tweet.user.friends_count)
    print("Нравится: ",tweet.user.favourites_count)
    print("Дата регистрации: ",tweet.user.created_at)
    print("Количество твитов: ",tweet.user.statuses_count)
#    print("Количество твитов: ",tweet.quoted_status.retweet_count)    
    try:
        if type(tweet.quoted_status.retweet_count)!='NoneType':
         print("Количество ретвитов: ",tweet.quoted_status.retweet_count) 
    except Exception:
         print("Количество ретвитов = 0")
         
    print("==============================================================")
    print("Данные по твиту: ")
    print("Количество ретвитов: ",tweet.retweet_count)    
    try:
        if type(tweet.retweeted_status.favorite_count)!='NoneType':
         print("Количество отметок 'Нравится': ",tweet.retweeted_status.favorite_count)
    except Exception:
         print("Количество отметок 'Нравится': 0")
         
    print("==============================================================")
    print("Оценка доверия к пользователю")
    regYears = datetime.date.today().year 
    Credibility(tweet.user.verified)
    Role(tweet.user.followers_count,tweet.user.friends_count)
    Influence(tweet.user.statuses_count)
