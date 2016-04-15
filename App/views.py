# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from App.models import App
from datetime import datetime
#处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
# Create your views here.

def home(request):
    post_list = App.objects.all()
    return render(request,'home.html',{'post_list': post_list})
    return HttpResponse('Hello World, Django')

def detail(request,my_args):
    post = App.objects.all()[int(my_args)]
    str = ("title = %s, category = %s,date_time = %s,content = %s"
           %(post.title,post.category,post.date_time,post.content))

    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})