# -*- coding: utf-8 -*-
"""Diango2 URL Configuration
网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from App.views import RSSFeed

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #可以使用设置好的url 进入网站后台
    url(r'^$', 'App.views.home'), #由于目前只有一个app, 方便起见, 就不设置include了

    url(r'^test/$','App.views.test'),

    url(r'$','App.views.home',name='home'),
    url(r'^(?P<id>\d+)/$','App.views.detail',name='detail'),
    url(r'^feed/$',RSSFeed(),name = "RSS"),
]
