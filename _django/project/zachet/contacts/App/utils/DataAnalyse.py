# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:47:33 2018
#     Оценка данных полученного текса с помощью метрик:
#       RTCheck: Определяет ретвит это или нет 
#       RT_DeL: Удаляет метки ретвита
#       Hashtags: Получение хэштегов из текста(если они присутсвуют)
#       Word_Count: Подсчет слов в тексте
#       Abr_Find: Поиск абвиатур и сокращений слов
#       Vulgar_Find: Поиск вульгарных слов
#       Mean_Find: Поиск слов указывающих на мнение
#       emoji_Find: Поиск смайлов и определение их эмоционального оттенка
#       url_find: Поиск ссылок
#       retweet_count: Счетные данные по твиту
@author: Alexandr
"""
import pandas as pd

def RT_DeL(text:list):
    if ('RT') in text:
        del text[0]
        del text[1]
        print('После удаления RT: ',len(text))
        return text
    else:
        return text

def RTCheck(text):
    if ('RT') in text:
        return True
    else:
        return False

def RTCheckToDel(text):
    if ('RT') in text:
        return RT_DeL(text)
    else:
        return False
    
def Hashtags(tm):
    i = 0
    if tm.hashtags!=[]:
        while i<=len(tm.hashtags):
            return print('Хештеги: ',tm.hashtags[i].text)
            i+=1
    else: 
            return print('Хештеги: отсутсвуют')  

def Word_Count(tm):
    tls = (tm).split()
    print('Количество слов в сообщении: {} '.format(len(tls)))
#    tm = RTCheck(tls)
    count = 0
    allword_count = len(tls)
    for word in tls:
        count+=len(word)
    print('Среднее количество символов в слове: {} \n'.format((count/allword_count)))
    
def Abr_Find(tm):
    abr = pd.read_excel('...\\data\\Список сокращений.xlsx')
    for word in abr['Abr']:
        if tm.find(word)>=0:
            print(word)
            
def Vulgar_Find(tm):
    abr = pd.read_excel('.//data//Список Вульгарных слов.xlsx')
    for word in abr['vul']:
        if tm.find(word)>=0:
            print(word)
            
def Mean_Find(tm):
    abr = pd.read_excel('.//data//Слова мнения.xlsx')
    for word in abr['mean']:
        if tm.find(word)>=0:
            print(word)
          
def Emoji_Find(tm):
    abr = pd.read_excel('.//data//Список смайлов.xlsx')
    for word in abr['emoj']:
        if tm.find(word)>=0:
            print(word)

def url_find(tm):
    i = 0
    if tm.urls!=[]:
        while i<=len(tm.urls):
            return print('urls: ',tm.urls[i].expanded_url)
    else: 
            return print('urls: отсутсвуют')  
    
def retweet_count(tweet):
   try:
       if type(tweet.retweet_count)!='NoneType':
             return tweet.retweet_count
   except Exception:
             print("Количество ретвитов = 0")

def favorite_count(timeline):
    try:
        if type(timeline.favorite_count)!='Null':
         return timeline.favorite_count
    except Exception:
         return print("Данные отсутствуют")
