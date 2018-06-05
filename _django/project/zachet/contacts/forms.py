from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contacts.models import query_data

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user

class queryform(forms.ModelForm):
    search_text = forms.CharField(max_length=500,required=True, widget=forms.TextInput(
        attrs ={
            'class':'form-control',
            'aria-label':'Username',
            'placeholder':'Введите слова по которым осуществляется поиск',
        }
    ))

    lang = forms.CharField(required=True, widget=forms.TextInput(
        attrs ={
            'class':'form-control',
            'aria-label':'Username',
            'placeholder':'Введите язык',
        }
    ))
    count = forms.CharField(required=True, widget=forms.TextInput(
        attrs ={
            'class':'form-control',
            'aria-label':'With textarea',
            'aria-label':'Username',
            'placeholder':'Введите количество',
        }
    ))

    from_data = forms.DateField(required=True, widget=forms.SelectDateWidget(
        attrs ={
            'class':'form-control',
            'aria-label':'Username',
            'placeholder':'%Y-%m-%d',
        }
    ))

    to_data = forms.DateField(required=True, widget=forms.SelectDateWidget(
        attrs ={
            'class':'form-control',
            'aria-label':'Username',
            'placeholder':'%Y-%m-%d',
        }
    ))

    def __init__(self, *args, **kwargs):
        super(queryform, self).__init__(*args, **kwargs)
        self.fields['search_text'].label = "Ваше слова:"
        self.fields['lang'].label = "Ваш язык:"
        self.fields['count'].label = "Количество"
        self.fields['from_data'].label = "От"
        self.fields['to_data'].label = "До"
    
    class Meta:
        model = query_data
        fields = ('search_text','lang','count','from_data','to_data',)