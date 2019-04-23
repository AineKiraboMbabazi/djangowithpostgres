from django.shortcuts import render
from django.http import HttpResponse


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)