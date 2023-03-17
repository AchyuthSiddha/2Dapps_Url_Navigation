from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('Virat/',Virat,name='Virat'),
    path('ABD/',ABD,name='ABD'),
]