from django.shortcuts import render

from django.http import HttpResponse

#from .models import Folder

def index(request):
	return HttpResponse('<p>My Computer2344242</p>')

def index1(request):
	return HttpResponse('<h2>Daphne Joan pierce</h2>')