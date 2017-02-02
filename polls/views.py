from django.shortcuts import render

from django.http import HttpResponse

import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def expo(req):
	return HttpResponse('<h1>Hello World</h1> <p> Good Morning!</p>')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def expound(request, expounding):
	return HttpResponse("Expounding on %s!!!" % expounding)