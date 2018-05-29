from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs ={
            'class':'form-control',
            'aria-label':'Username',
            'placeholder':'Введите Имя',
        }
    ))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs ={
            'class':'form-control',
            'type':'email',
            'aria-label':'Username',
            'placeholder':'Введите Email',
        }
    ))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs ={
            'class':'form-control',
            'aria-label':'With textarea',
            'aria-label':'Username',
            'placeholder':'Введите Текст',
        }
    ))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Ваше Имя:"
        self.fields['contact_email'].label = "Ваш email:"
        self.fields['content'].label = "Что вы хотите нам сообщить?"

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
