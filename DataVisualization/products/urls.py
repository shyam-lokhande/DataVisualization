from .views import *

from django.urls import path

app_name='products'
urlpatterns=[
    path('',chart_select_view,name='main-products-view'),
    path('add/',add_purchase,name='add-purchase'),
    path('sales/',sales_dist_view,name='sales-view')
]
