from .views import *

from django.urls import path

app_name='customers'
urlpatterns=[
    path('',Customer_corr_view,name='main-customers-view'),
]
