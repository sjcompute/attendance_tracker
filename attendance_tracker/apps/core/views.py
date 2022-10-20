from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SchoolSerializer
from apps.school.models import School
# Create your views here.



class SchoolView(viewsets.ModelViewSet):
   queryset = School.objects.all()
   serializer_class = SchoolSerializer



