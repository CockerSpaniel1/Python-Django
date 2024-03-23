
#custom cafe 內的 urls.py
from django.urls import path
from . import views

urlpatterns =[
    path('tea/',views.tea),
    path('tea1/',views.tea1),
]