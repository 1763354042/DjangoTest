from django.shortcuts import render
from .models import Salaryrange
from .models import AvgSalary
from .models import Citylist
from .models import Citysalary
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'JobData/index.html')

def top(request):
    return render(request,'JobData/top.html')

def analysis(request):
    return render(request,'JobData/analysis.html')

def data(request):
    return render(request,'JobData/data.html')

def page(request):
    keyword = request.GET.get('keyWord')
    print(keyword+'123')
    rep = render(request,'JobData/page.html')
    rep.set_cookie("keyWord",keyword)
    return rep

def post(request):
    return render(request,'JobData/post.html')

def Recommend(request):
    return render(request,'JobData/Recommend.html')

def get_avg_salary(request):
    keyword = request.COOKIES["keyWord"]
    avg = AvgSalary.objects.filter(keyword = keyword)
    avg_dic = {}
    avg_dic["keyWord"] = avg[0].keyword
    avg_dic["avgsalary"] = avg[0].avgsalary
    return JsonResponse(avg_dic)

def get_city_list(request):
    keyword = request.COOKIES["keyWord"]
    avg = Citylist.objects.filter(keyword = keyword)
    return JsonResponse(avg[0])

def get_city_salary(request):
    keyword = request.COOKIES["keyWord"]
    avg = Citysalary.objects.filter(keyword = keyword)
    return JsonResponse(avg)

def get_salary_range(request):
    keyword = request.COOKIES["keyWord"]
    avg = Salaryrange.objects.filter(keyword = keyword)
    return JsonResponse(avg)