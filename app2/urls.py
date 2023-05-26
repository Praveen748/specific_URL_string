from django.urls import path
from app2.views import *
app_name='powerstar'
urlpatterns=[
    path('dhiraj/',dhiraj,name='dhiraj'),
    path('aakash/',aakash,name='aakash'),
    path('dr_amma/',dr_amma,name='dr_amma'),
    
]