from django.shortcuts import render, redirect
from django import apps
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import School
# Create your views here.

def SchoolView(request):
    Schools = School.objects.all() 

    return render(request, 'school/base.html', {'Schools': Schools})
