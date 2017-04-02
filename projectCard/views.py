from django.shortcuts import render

from django.http import HttpResponse

from .models import Card

def home(request):
	return render(request, 'projectCard/home.html')

def project(request):
	cards = Card.objects.all()
	return render(request, 'projectCard/project.html', { 'cards' : cards})