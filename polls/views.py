from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
# Create your views here.
from .models import Question


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
#    output= ', '.join([q.question_text for q in last_question])
    context = {
        "last_question_list": last_question_list,
    }
    return HttpResponse(template.render(context, request))


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Dose not exist")
    return render(request, 'polls/detail.html', {'question': question})

#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
