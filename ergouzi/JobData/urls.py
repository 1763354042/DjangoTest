from django.urls import path
from . import views

urlpatterns =[
    path('index',views.index,name = 'index'),
    path('top',views.top,name = 'top'),
    path('analysis',views.analysis,name = 'analysis'),
    path('data',views.data,name = 'data'),
    path('page',views.page,name = 'page'),
    path('post',views.post,name = 'post'),
    path('get_avg_salary',views.get_avg_salary,name = 'get_avg_salary'),
    path('get_city_list',views.get_city_list,name = 'get_city_list'),
    path('get_city_salary',views.get_city_salary,name = 'get_city_salary'),
    path('get_salary_range',views.get_salary_range,name = 'get_salary_range'),
    path('Recommend',views.Recommend,name = 'Recommend'),
]