from django.shortcuts import render, redirect
from django import apps
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Teacher
# Create your views here.

def TeacherView(request):
    Teachers = Teacher.objects.all() 

    return render(request, 'teacher/base.html', {'Teachers': Teachers})