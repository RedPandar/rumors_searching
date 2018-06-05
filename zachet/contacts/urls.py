from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('video',views.video,name='video'),
    path('plot',views.plot,name='plot'),
]