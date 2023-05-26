from django.urls import path
app_name='impact'
from app1.views import *
urlpatterns=[
    path('praveen/',praveen,name='praveen'),
    path('kushal/',kushal,name='kushal')
]