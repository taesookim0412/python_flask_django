"""quotedash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'quotes$', views.quotes),
    url(r'addquote$', views.addquote),
    url(r'user/(?P<id>\d+)$', views.userquotes),
    url(r'editaccount$', views.editaccount),
    url(r'updateaccount$', views.updateaccount),
    url(r'logout$', views.logout),
    url(r'delete$', views.delete)
    # url(r'user/(?P<id>\d+)$', views.viewuser),
    # url(r'myaccount/(?P<id>\d+)$', views.myaccount),
    # url(r'quotes', views.quotes),
]
