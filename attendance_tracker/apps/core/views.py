from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SchoolSerializer
from .serializers import TeacherSerializer
from apps.school.models import School
from apps.teacher.models import Teacher
# Create your views here.



class SchoolView(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = SchoolSerializer

class TeacherView(viewsets.ModelViewSet):
   queryset = Teacher.objects.all()
   serializer_class = TeacherSerializer


