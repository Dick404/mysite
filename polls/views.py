from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, question_id):
    return HttpResponse("hello world.You are at the polls %s." % question_id)


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def detail(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
