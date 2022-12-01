from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
def student(render):
    print('test')
    return HttpResponse('student') 