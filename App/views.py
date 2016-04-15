# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from App.models import App
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed  #注意加入import语句
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger #添加包


#处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
# Create your views here.

def home(request):
    posts = App.objects.all(); #获取全部的App对象
    paginator = Paginator(posts,2) #每页显示两个
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list': post_list})
    #return HttpResponse('Hello World, Django')

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})

def detail(request,id):
    try:
        post = App.objects.get(id = str(id))
    except App.DoesNotExist:
        raise Http404

    return render(request,'post.html',{'post':post})

class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return App.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.add_date

    def item_description(self, item):
        return item.content