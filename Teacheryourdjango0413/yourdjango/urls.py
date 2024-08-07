"""
URL configuration for yourdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from order.views import index,products,signup,signupok,register,member,logout,login,update,updateok,delete

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', index),
    path('products/', products),
    path('signup/', signup),
    path('signupok/', signupok),
    path('register/', register),
    path('member/', member),
    path('logout/', logout),
    path('login/', login),
    path('update/<str:email>', update),
    path('updateok/', updateok),
    path('delete/<str:email>', delete),
]
