# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:27:18 2018
#   slogi - Подсчет слогов в предложении.   
#   Word_Count - Подсчет слов в предложении.
#
#
#
#
#
@author: Alexandr
"""

def slogi(text, lang):
    K=0
    if lang=='ru':
        for x in text:
            if x in ('аеёиоуыэюя'):
                K+=1
        print(K)
        return K
    elif lang=='eng':
        for x in text:
            if x in ('aeiou'):
                K+=1
        print(K)
        return K
    else:
        return print('Текст не поддается подсчету')

def Word_Count(tm):
    tls = (tm).split()
    print('Количество слов в сообщении: {} '.format(len(tls)))
#    tm = RTCheck(tls)
    count = 0
    allword_count = len(tls)
    for word in tls:
        count+=len(word)
    print('Среднее количество символов в слове: {} \n'.format((count/allword_count)))