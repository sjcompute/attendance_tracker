from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TeacherSerializer
from .serializers import ClassesSerializer
from apps.teacher.models import Teacher
from apps.classes.models import Classes
# Create your views here.


class TeacherView(viewsets.ModelViewSet):
   queryset = Teacher.objects.all()
   serializer_class = TeacherSerializer

class ClassesView(viewsets.ModelViewSet):
   queryset = Classes.objects.all()
   serializer_class = ClassesSerializer
