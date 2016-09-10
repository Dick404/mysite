from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Question, Choice

'''

def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
#    output= ', '.join([q.question_text for q in last_question])
    context = {
        "last_question_list": last_question_list,
    }
    return HttpResponse(template.render(context, request))


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
#    response = "You're looking at the results of question %s."
    return render(request, "polls/result.html", {'question': question, "question_id": question_id})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Dose not exist")
    return render(request, 'polls/detail.html', {'question': question})

#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            "error_message": "You didn't select a Choice",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
#    response = "You're looking at the results of question %s."
    return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))
'''


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'last_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            "error_message": "You didn't select a Choice",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        #    response = "You're looking at the results of question %s."
    return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))