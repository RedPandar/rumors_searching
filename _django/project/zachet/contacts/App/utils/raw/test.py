# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:43:42 2018

@author: Alexandr
"""
import twitter

api = twitter.Api(consumer_key='EzWpyK9RyrOeRpgrefXdvXjrg',
    consumer_secret='IdHd4fMbobMujDITJHJ4wpFZ4vlcZxO68r5ofQhrR8l9gUqHGo',
    access_token_key = 	"296713992-YdgVZFM3requrT7s5aVMbav8hXonttWLZmvgBWam",
    access_token_secret=	"G1zujW6QStwMlbagvSrjf0s46IDsItfvWF5v0O3lZXLUW")

q = "q=Pokemon"
lang = "ru"
count = "count=1"
query = q+"&"+lang+"&"+count
for tweet in api.GetSearch(raw_query=query):
    replies = api.GetMentions(tweet.user.id) 
    
    retweets_count = api.GetUserRetweets(tweet.user.id)
    print(retweets_count,len(retweets_count))
    
    user_data_and_last_message = api.GetUser(tweet.user.id)
#    print(user_data_and_last_message)
    
    followers_id = api.GetFollowerIDsPaged(tweet.user.id)
#    print(followers_id)
    
    test4 = api.GetBlocks()
    
    test5 = api.GetReplies()
    