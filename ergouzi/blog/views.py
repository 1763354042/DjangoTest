from django.shortcuts import render

# Create your views here.
#coding:utf8

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect                  #记得导入该模块
from .models import Question,Choice
from django.urls import reverse
from django.template import loader
# def index(request):
#     return HttpResponse("<h1>hello Django!123</h1>")     #网页输出"hello Django!"

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # return HttpResponse(output)
    # return HttpResponse(template.render(context,request))
    return render(request,'blog/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html', {'question': question})

def result(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request,question_id):
    # return HttpResponse("You're voting on questions %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))