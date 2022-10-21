from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from apps.classes.models import Classes
from apps.teacher.models import Teacher
from apps.attendance.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('State', 'Date')


class ClassesSerializer(serializers.ModelSerializer):
    State = AttendanceSerializer(many=True)
    Date = AttendanceSerializer(many=True)
    
    class Meta:
       model = Classes
       fields = ('Class_id', 'Student_id', 'State', 'Date')
    #    fields = ('Teacher_id', 'Class_id', 'Student_id')

class TeacherSerializer(serializers.ModelSerializer):
    Class_id = ClassesSerializer(many=True)

    class Meta:
       model = Teacher
       #fields = '__all__'
       fields = ('Teacher_id', 'Class_id')
       
