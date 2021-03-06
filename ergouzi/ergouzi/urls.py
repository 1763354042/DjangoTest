"""ergouzi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
#coding:utf8

from django.conf.urls import url
from django.contrib import admin
# from blog import views as blog_views            #记住！先导入app中的views后使用
app_name = 'blog'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',blog_views.index,name='index'),
    path('blog/',include('blog.urls')),           #include允许引用其他URLconfs
    path('JobData/',include('JobData.urls'))               #include允许引用其他URLconfs

]