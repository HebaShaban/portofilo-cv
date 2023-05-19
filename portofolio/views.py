from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def Welcome(request):
 return HttpResponse("Welcome to our site")
# Create your views here.

def Welcome(request):
 template = loader.get_template('cv.html')
 return HttpResponse(template.render())

