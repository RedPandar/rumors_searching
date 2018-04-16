# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:52:03 2018

twitter rumors_analisation
@author: Alexandr
"""


import twitter
import datetime
from time import ctime
import io, json
import pandas as pd

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

table = pd.DataFrame(columns=['Name', 'ID', 'Verified', 'followers_count', 'friends_count', 'favourites_count', 'created_at', 'statuses_count', 'Credibility', 'Originallity', 'Influence', 'Role', 'Engagement'])

# =============================================================================
# Блок Функций проверки
# =============================================================================

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
    try:
        if type(followers/followees)!=0:
         return print("Role = ",followers/followees) 
    except ZeroDivisionError:
         return print("Role = ",0) 
    

def Engagement(tweets:int,retweets:int,replies:int,favorites:int,acc_age:int):
    return print("Engagement = ",(tweets+retweets+replies+favorites)/(acc_age))


# =============================================================================
# Блок вызова и вывода
# =============================================================================
count = 0
for tweet in api.GetSearch(raw_query="q=TheWalkingDead&result_type=text&count=10&src=hash"):
    with io.open('tweet.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tweet._json, ensure_ascii=False))

    print("\n==============================================================")
    
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
#    print("Количество твитов: ",timeline.retweet_count)    
    try:
        if type(timeline.retweet_count)!='NoneType':
         print("Количество ретвитов: ",timeline.retweet_count) 
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
    credibility = Credibility(tweet.user.verified)
    role = Role(tweet.user.followers_count,tweet.user.friends_count)
    inf = Influence(tweet.user.statuses_count)
    
# =============================================================================
#Блок записи в датафрейм
# =============================================================================
    table.loc[count] = ([tweet.user.screen_name, tweet.user.id, tweet.user.verified,tweet.user.followers_count, tweet.user.friends_count, tweet.user.favourites_count, tweet.user.created_at, tweet.user.statuses_count, credibility, 0, tweet.user.statuses_count, role, 0])
    count +=1