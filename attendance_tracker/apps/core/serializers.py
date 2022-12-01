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
        fields = ('state', 'date', 'student_id', 'class_id','id')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'first_name', 'last_name', 'class_id')
        #fields = '__all__'

class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
       model = Classes
       fields = ('class_id', 'teacher_id', 'student_id')
    
class TeacherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
       model = Teacher
       #fields = '__all__'
       fields = ('teacher_id', 'class_id')
       
