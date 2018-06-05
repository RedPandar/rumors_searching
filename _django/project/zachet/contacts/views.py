from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.template.loader import get_template
from contacts.forms import RegistrationForm,queryform
import twitter
import datetime
from django.http import HttpResponse
from .App import main
from contacts.models import query_data, query_data_analyse
import django_tables2 as tables
from django.contrib.auth.decorators import login_required

class class_table(tables.Table):
    class Meta:
        model = query_data
        attrs = {'class': 'table table-hover'}

class index(TemplateView):
    template_name = 'Zachet_temp/index.html'
    def get(self,request):
        if request.user.is_anonymous==False:
            form = queryform()
            table_class = class_table(query_data.objects.filter(user=request.user))
            context = {'form':form, 'past_query': table_class}
            return render(request,self.template_name,context)
        else:
            return redirect('login')

    def post(self,request):
        form = queryform(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.user = request.user
            query.save()
            search_text = request.POST.get('search_text', '')
            lang = request.POST.get('lang','')
            count = request.POST.get('count', '')
            from_data = request.POST.get('from_data', '')
            To = request.POST.get('to_data', '')
            context = {
                'search_text': search_text,
                'lang': lang,
                'count': count,
                'from_data': from_data,
                'to_data': To,
            }
            main.twtt(search_text,lang,count,from_data,To)
            return redirect('query')
        return render(request,self.template_name, {
            'form': form,
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
    
def logout(request):
    return redirect('index')

def query(request):
    all_entries = query_data.objects.all()
    last_entries = query_data.objects.last()
    template = get_template('Zachet_temp/query.html')
    context = {'all_entries':all_entries,'last_entries':last_entries,}
    return HttpResponse(template.render(context))