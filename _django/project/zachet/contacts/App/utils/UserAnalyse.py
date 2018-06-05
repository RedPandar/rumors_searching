# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:15:19 2018
#     Оценка данных пользователя с помощью метрик:
#       Credibility: Достоверность - определяет наличие отметки Verify для пользователя.
#       Originallity: Оригинальность - процент оригинальных твитов, а не ретвитов
#       Influence: Поток - Количество твитов пользователя в совокупностью с ретвитами
#       Role: Роль - определяет роль пользователя в зависимости от соотношения фоловеров и читаемых
#       Engagement: Вовлеченность - определетяет активность пользователя за время существования аккаунта
@author: Alexandr Chernyaev
"""

def Credibility(verified:bool):
    if verified ==True:
     return 1
    else:
     return 0
    
def Originallity(twt_count:int,retwt_count:int):
    if retwt_count == 0:
        return 1
    else:
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