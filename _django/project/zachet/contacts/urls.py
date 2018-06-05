from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(),name='index'),
    path('register',views.register,name='register'),
    path('query',views.query,name='query'),
]