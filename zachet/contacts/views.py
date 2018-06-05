from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.template.loader import get_template
from contacts.forms import RegistrationForm
from .forms import ContactForm
from .forms import queryform
from django.contrib import messages
import twitter
import datetime
from time import ctime,sleep
import io, json
import pandas as pd
import numpy as np
import random
from django.http import HttpResponse

def index(request):
    form_class = queryform
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            Word_line = request.POST.get(
                'Word_line'
            , '')
            contact_email = request.POST.get(
                'lang'
            , '')
            form_content = request.POST.get('content', '')

            context = {
                'Word_line': Word_line,
                'lang': lang,
                'form_content': form_content,
            }

            messages.success(request, 'Ваше сообщение доставлено!')
            return redirect('contact')

    return render(request,'Zachet_temp/index.html', {
        'form': form_class,
    })

def register(request):
    if request.method == 'POST':
     form = RegistrationForm(request.POST)
     if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']

         user = authenticate(username=username, password=password)
         login(request,user)
         return redirect('index')
    else:
     form = RegistrationForm()

    contex = {'form' : form}
    return render(request,'Registration/register.html',contex)

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            template =   get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Ваше сообщение доставлено!')
            return redirect('contact')

    return render(request, 'Zachet_temp/contact.html', {
        'form': form_class,
    })

def profile(request):
    return render(request,'Zachet_temp/profile.html')

def logout(request):
    return redirect('index')

def video(request):
    return render(request,'Zachet_temp/video.html')

def plot(request):
        api = twitter.Api(consumer_key='EzWpyK9RyrOeRpgrefXdvXjrg',
        consumer_secret='IdHd4fMbobMujDITJHJ4wpFZ4vlcZxO68r5ofQhrR8l9gUqHGo',
        access_token_key = 	"296713992-YdgVZFM3requrT7s5aVMbav8hXonttWLZmvgBWam",
        access_token_secret=	"G1zujW6QStwMlbagvSrjf0s46IDsItfvWF5v0O3lZXLUW")

        table = pd.DataFrame(columns=['Name', 'ID', 'Verified', 'followers_count', 'friends_count', 'favourites_count', 'created_at', 'statuses_count','Geo','Time Zone', 'Credibility', 'Originallity', 'Influence', 'Role', 'Engagement','text'])
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

        count = 0
        for i in range(5):
            for tweet in api.GetSearch(raw_query="q=Telegram&src=tren&count=1"):
                with io.open('tweet.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(tweet._json, ensure_ascii=False))
            
                timeline = api.GetUserTimeline(tweet.user.id, count=1) 
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

                table.loc[i] = ([tweet.user.screen_name, tweet.user.id, tweet.user.verified,tweet.user.followers_count, tweet.user.friends_count, tweet.user.favourites_count, tweet.user.created_at, tweet.user.statuses_count,tweet.user.lang,tweet.user.time_zone, credibility, originallity, tweet.user.followers_count, role, engagement,timeline[0].text])
                count +=1


        return HttpResponse(table.to_html(classes='table table-striped table-dark'))