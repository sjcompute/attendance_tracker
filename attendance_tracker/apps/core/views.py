from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TeacherSerializer
from .serializers import ClassesSerializer
from .serializers import AttendanceSerializer
from .serializers import StudentSerializer
from apps.teacher.models import Teacher
from apps.classes.models import Classes
from apps.student.models import Student
from apps.attendance.models import Attendance
# Create your views here.

class AttendanceView(viewsets.ModelViewSet):
   queryset = Attendance.objects.all()
   serializer_class = AttendanceSerializer
   def get_queryset(self):
      studentid = self.request.GET.get('student_id', '')
      classid = self.request.GET.get('class_id', '')
      # print(studentid)
      # print(classid)
      print(Attendance.objects.all())
      if studentid != '' and classid != '':
         return Attendance.objects.filter(Student_id=studentid, Class_id=classid)
      elif studentid != '':
         return Attendance.objects.filter(Student_id=studentid)
      elif classid != '':
         return Attendance.objects.filter(Class_id=classid)
      #return Attendance.objects.filter(Student_id=studentid, Class_id=classid)
class StudentView(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

class TeacherView(viewsets.ModelViewSet):
   queryset = Teacher.objects.all()
   serializer_class = TeacherSerializer

class ClassesView(viewsets.ModelViewSet):
   queryset = Classes.objects.all()
   serializer_class = ClassesSerializer
