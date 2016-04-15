# -*- coding: utf-8 -*-

from django.db import models
#与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。
from django.core.urlresolvers import  reverse

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=100) #博客题目
    category = models.CharField(max_length= 50,blank=True) #博客标签
    date_time = models.DateTimeField(auto_now_add=True) #博客日期
    content = models.TextField(blank=True,null = True) #博客文章正文

    def get_absolute_url(self):
        path = reverse('detail', dwargs={'id': self.id})
        return 'http://1270.0.0.1:8080%s' % path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


