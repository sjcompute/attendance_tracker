from django.apps import apps
from django.db import models

#from apps.classes.models import Classes
# Create your models here.
class Teacher(models.Model):
    #class Meta:
    #   abstract = True

    teacher_id = models.CharField(max_length=32, primary_key=True)
    class_id = models.ManyToManyField('classes.Classes', blank=True)
    #student_id = models.ManyToManyField('student.Student', blank=True)


    def __str__(self):
        return self.teacher_id