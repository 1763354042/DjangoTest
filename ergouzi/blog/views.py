from django.shortcuts import render

# Create your views here.
#coding:utf8

from django.shortcuts import render
from django.http import HttpResponse                  #记得导入该模块

def index(request):
    return HttpResponse("<h1>hello Django!123</h1>")     #网页输出"hello Django!"