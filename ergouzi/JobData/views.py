from django.shortcuts import render
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
    keyWord = request.GET.get('keyWord')
    return render(request,'JobData/page.html',{'keyWord':keyWord})

def post(request):
    return render(request,'JobData/post.html')

def Recommend(request):
    return render(request,'JobData/Recommend.html')