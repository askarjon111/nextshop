from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>', product_detail, name='product_detail'),
]
