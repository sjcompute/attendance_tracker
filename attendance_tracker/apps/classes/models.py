from django.db import models
from django.apps import apps

from apps.school.models import School
from apps.teacher.models import Teacher
# Create your models here.
class Classes(models.Model):
    #class Meta:
    #   abstract = True
    Class_id = models.CharField(max_length=32, primary_key=True)
    School_id = models.ForeignKey('school.School', on_delete=models.PROTECT, blank=True, null=True)
    Teacher_id = models.ForeignKey('teacher.Teacher', blank=True, on_delete=models.PROTECT)
    Student_id = models.ManyToManyField('student.Student', blank=True)

    def __str__(self):
        return self.Class_id