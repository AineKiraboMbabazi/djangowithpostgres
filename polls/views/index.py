from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from ..models import Question
# Create your views here.


def index(request):
 
    questions = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    
    context = {
        'questions':questions,
    }
    return HttpResponse(template.render(context,request))