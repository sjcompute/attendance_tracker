from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.school.models import School
from apps.teacher.models import Teacher

class SchoolSerializer(serializers.ModelSerializer):
   class Meta:
       model = School
       fields = ('School_id', 'Teacher_id', 'Student_id', 'Class_id',)


    
class TeacherSerializer(serializers.ModelSerializer):
   class Meta:
       model = Teacher
       fields = ('School_id', 'Teacher_id', 'Student_id', 'Class_id',)