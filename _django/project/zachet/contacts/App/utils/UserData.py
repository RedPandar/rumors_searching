# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:15:19 2018
#     Данных пользователя с помощью метрик:
#       screen_name: Отображаемое имя пользователя
#       user_id: ID пользователя
#       user_verified: проверка пользователя
#       followers_count: Количество подписчиков
#       friends_count: количество читаемых пользователей
#       created_at: дата создания аккаунта
#       statuses_count: количество твитов
#       retweet_count: количество ретвитов
#       time_zone: Временная зона
#       registration_years: количество лет с регистрации
@author: Alexandr Chernyaev
"""
import datetime
from . import DataAnalyse

def screen_name(tweet):
    try:
        if type(tweet.user.screen_name)!='Null':
         return tweet.user.screen_name
    except Exception:
         return print("Данные отсутствуют")

def user_id(tweet):
    try:
        if type(tweet.user.id)!='Null':
         return tweet.user.id
    except Exception:
         return print("Данные отсутствуют")

def user_verified(tweet):
    try:
        if type(tweet.user.verified)!='Null':
         return tweet.user.verified
    except Exception:
         return print("Данные отсутствуют")

def followers_count(tweet):
    try:
        if type(tweet.user.followers_count)!='Null':
         return tweet.user.followers_count
    except Exception:
         return print("Данные отсутствуют")

def friends_count(tweet):
    try:
        if type(tweet.user.friends_count)!='Null':
         return tweet.user.friends_count
    except Exception:
         return print("Данные отсутствуют")

def created_at(tweet):
    try:
        if type(tweet.user.created_at)!='Null':
         return tweet.user.created_at
    except Exception:
         return print("Данные отсутствуют")

def statuses_count(tweet):
    try:
        if type(tweet.user.statuses_count)!='Null':
         return tweet.user.statuses_count
    except Exception:
         return print("Данные отсутствуют")
     
def retweet_count(tweet,api):
    rt_count = 0
    uid = user_id(tweet)
    timeline = api.GetUserTimeline(uid, count=100)
    if DataAnalyse.RTCheck(timeline[0].text)==True:
        rt_count +=1
    return rt_count

def time_zone(tweet):
        try:
            if type(tweet.user.time_zone)!='Null':
             return tweet.user.time_zone
        except Exception:
         return print("Данные отсутствуют")
         
def registration_years(tweet):
    date = (tweet.user.created_at).split()
    regYears = datetime.date.today().year-int(date[5])
    return regYears