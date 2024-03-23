"""
URL configuration for mydjango project.

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
from django.urls import path,include
from cafe.views import index,coffee,slogan,history,coffee1,coffee2,coffee6,coffee3,coffee4,coffee5,coffee6,coffee7,coffee8,coffee9,coffee10,coffee11,mycookie1,mycookie2,mycookie3,mycookie4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffee',coffee)
]

urlpatterns +=[
    path('',index)
]

urlpatterns +=[
    path('slogan',slogan),
    path('history',history)
]


urlpatterns +=[
    path('coffee1',coffee1),
    path('coffee2',coffee2),
    path('coffee3',coffee3),
    path('coffee4',coffee4),
    path('coffee5',coffee5),
    path('coffee6',coffee6),
    path('coffee7',coffee7),
    path('coffee8',coffee8),
    path('coffee9/<str:pid>/',coffee9),
    path('coffee10',coffee10),
    path('coffee11',coffee11),
]

urlpatterns +=[
    path('',include('cafe.urls')),
]


urlpatterns +=[
    path('mycookie1/',mycookie1),
    path('mycookie2/',mycookie2),
    path('mycookie3/',mycookie3),
    path('mycookie4/',mycookie4),
]

































urlpatterns +=[
  
    path('coffee6',coffee6),
]

