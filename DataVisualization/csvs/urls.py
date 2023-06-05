from .views import *

from django.urls import path

app_name='products'
urlpatterns=[
    path('',uploadFile,name='upload-view'),
]
