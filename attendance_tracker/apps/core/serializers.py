from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from apps.classes.models import Classes
from apps.teacher.models import Teacher
from apps.attendance.models import Attendance
from apps.student.models import Student
class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ('State', 'Date', 'id')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('Student_id', 'First_name', 'Last_name', 'Class_id')
        #fields = '__all__'

class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
       model = Classes
       fields = ('Class_id', 'Teacher_id', 'Student_id')
    
class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
       model = Teacher
       #fields = '__all__'
       fields = ('Teacher_id', 'Class_id')
       
