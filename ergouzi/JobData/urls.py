from django.urls import path
from . import views

urlpatterns =[
    path('index',views.index,name = 'index'),
    path('top',views.top,name = 'top'),
    path('analysis',views.analysis,name = 'analysis'),
    path('data',views.data,name = 'data'),
    path('page',views.page,name = 'page'),
    path('post',views.post,name = 'post'),
    path('Recommend',views.Recommend,name = 'Recommend'),
]