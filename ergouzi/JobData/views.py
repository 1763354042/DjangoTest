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
    rep = render(request,'JobData/page.html')
    rep.set_cookie("keyWord",keyword)
    return rep

def post(request):
    return render(request,'JobData/post.html')

def Recommend(request):
    return render(request,'JobData/Recommend.html')

def get_avg_salary(request):
    avgSalaryList = []
    avg_salary = AvgSalary.objects.all()
    for item in avg_salary:
        avg_salary_dic = {}
        avg_salary_dic["keyWord"] = item.keyword
        avg_salary_dic["avgSalary"] = item.avgsalary
        avgSalaryList.append(avg_salary_dic)
    return JsonResponse(avgSalaryList,safe=False)

def get_city_list(request):
    cityListList=[]
    keyword = request.COOKIES["keyWord"]
    city_list = Citylist.objects.filter(keyword = keyword).order_by('value')[0:10]
    for item in city_list:
        cityListDic = {}
        cityListDic["keyWord"] = item.keyword
        cityListDic["city"] = item.city
        cityListDic["value"] = item.value
        cityListList.append(cityListDic)
    return JsonResponse(cityListList,safe=False)

def get_city_salary(request):
    citySalaryList = []
    keyword = request.COOKIES["keyWord"]
    citySalary = Citysalary.objects.filter(keyword = keyword)
    for item in citySalary:
        citySalaryDic = {}
        citySalaryDic["keyWord"] = item.keyword
        citySalaryDic["city"] = item.city
        citySalaryDic["salary"] = item.salary
        citySalaryList.append(citySalaryDic)
    return JsonResponse(citySalaryList,safe=False)

def get_salary_range(request):
    salaryRangeList = []
    keyword = request.COOKIES["keyWord"]
    salary_range = Salaryrange.objects.filter(keyword = keyword)
    for item  in salary_range:
        salaryRangeDic = {}
        salaryRangeDic["keyWord"] = item.keyword
        salaryRangeDic["range"] = item.range
        salaryRangeDic["num"] = item.num
        salaryRangeList.append(salaryRangeDic)
    return JsonResponse(salaryRangeList,safe=False)