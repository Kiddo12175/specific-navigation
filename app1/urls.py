from app1.views import *
from django.urls import path

app_name='somthing'

urlpatterns=[
    path('kiddo/',kiddo,name='kiddo'),
]