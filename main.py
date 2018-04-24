# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:52:03 2018

twitter rumors_analisation
@author: Alexandr
"""


import twitter
import datetime
from time import ctime,sleep
import io, json
import pandas as pd
import random

# =============================================================================
# Подключение к API Twitter
# =============================================================================
api = twitter.Api(consumer_key='EzWpyK9RyrOeRpgrefXdvXjrg',
consumer_secret='IdHd4fMbobMujDITJHJ4wpFZ4vlcZxO68r5ofQhrR8l9gUqHGo',
access_token_key = 	"296713992-YdgVZFM3requrT7s5aVMbav8hXonttWLZmvgBWam",
access_token_secret=	"G1zujW6QStwMlbagvSrjf0s46IDsItfvWF5v0O3lZXLUW")
app_name = "Rumors Searching"

# =============================================================================
# Блок организации датафрейма
# =============================================================================

table = pd.DataFrame(columns=['Name', 'ID', 'Verified', 'followers_count', 'friends_count', 'favourites_count', 'created_at', 'statuses_count','Geo','Time Zone', 'Credibility', 'Originallity', 'Influence', 'Role', 'Engagement'])

# =============================================================================
# Блок Функций проверки
# =============================================================================

def Credibility(verified:bool):
    if verified ==True:
     return 1
    else:
     return 0
     
def Originallity(twt_count:int,retwt_count:int):
    return twt_count/retwt_count

def Influence(Influence:int):
    return Influence

def Role(followers:int,followees):
    try:
        if type(followers/followees)!=0:
         return followers/followees
    except ZeroDivisionError:
         return 0 
    

def Engagement(tweets:int,retweets:int,replies:int,favorites:int,acc_age:int):
    try:
        if type(acc_age)!=0:
         return (tweets+retweets+replies+favorites)/(acc_age)
    except ZeroDivisionError:
         return (tweets+retweets+replies+favorites)/(0.99) 


# =============================================================================
# Блок вызова и вывода
# =============================================================================
count = 0
for i in range(1):
    for tweet in api.GetSearch(raw_query="q=Telegram&src=tren&count=1"):
        with io.open('tweet.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(tweet._json, ensure_ascii=False))
    
#        print("\n==============================================================")
        print(count)
        timeline = api.GetUserTimeline(tweet.user.id, count=1) 
        with io.open('timeline.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(tweet._json, ensure_ascii=False))
    
        print("Текст Твита: ",timeline[0].text)
        
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
        try:
            if type(timeline.retweet_count)!='NoneType':
             print("Количество ретвитов: ",timeline.retweet_count) 
        except Exception:
             print("Количество ретвитов = 0")
        
        try:
            if type(tweet.user.time_zone)!='Null':
             print("Локация : ",tweet.user.time_zone) 
        except Exception:
             print("Локация : Неизвестна")
             
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
        date = (tweet.user.created_at).split()
        regYears = datetime.date.today().year-int(date[5])
        print("Полных лет с регистрации: ",regYears)
        credibility = Credibility(tweet.user.verified)
        role = Role(tweet.user.followers_count,tweet.user.friends_count)
        inf = Influence(tweet.user.statuses_count)
        retweets = (tweet.user.statuses_count/100)*random.randint(1,50) 
        replies = (tweet.user.statuses_count/100)*random.randint(-25, 25)
        engagement = Engagement(tweet.user.statuses_count,retweets,tweet.user.favourites_count,replies,regYears)
        originallity = Originallity(tweet.user.statuses_count,retweets)
    # =============================================================================
    #Блок записи в датафрейм
    # =============================================================================
        table.loc[count] = ([tweet.user.screen_name, tweet.user.id, tweet.user.verified,tweet.user.followers_count, tweet.user.friends_count, tweet.user.favourites_count, tweet.user.created_at, tweet.user.statuses_count,tweet.user.lang,tweet.user.time_zone, credibility, originallity, tweet.user.followers_count, role, engagement])
        count +=1
        sleep(0.5)
#table.to_excel('out.xlsx')