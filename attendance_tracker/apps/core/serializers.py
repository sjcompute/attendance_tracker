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
        #fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    State = AttendanceSerializer(many=True)
    class Meta:
        model = Student
        fields = ('Student_id', 'First_name', 'Last_name', 'Class_id', 'State')
        #fields = '__all__'

class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    Student_id = StudentSerializer(many=True)
    #State = StudentSerializer(many=True)
    #State = serializers.SerializerMethodField()
    #Date = serializers.SerializerMethodField()
    
    class Meta:
       model = Classes
       fields = ('Class_id', 'Student_id')
       #fields = '__all__'
    #    fields = ('Teacher_id', 'Class_id', 'Student_id')
    
    # def get_State(self, Classes):
    #     attendance_state_query = Attendance.objects.filter(Class_id__Class_id__contains=Classes.Class_id)
    #     print(Attendance.objects.filter(Class_id__Class_id__contains=Classes.Class_id))
    #     #print(Attendance.objects.get(Class_id= ))
    #     #instance = self.Meta.model(**Classes.Class_id)
    #     print(Classes.Class_id)
    #     serializer = AttendanceSerializer(attendance_state_query, many=True)
        
    #     return serializer.data

    
class TeacherSerializer(serializers.ModelSerializer):
    Class_id = ClassesSerializer(many=True)

    class Meta:
       model = Teacher
       #fields = '__all__'
       fields = ('Teacher_id', 'Class_id')
       
