from django.apps import apps
from django.db import models

#from apps.classes.models import Classes
# Create your models here.
class Teacher(models.Model):
    #class Meta:
    #   abstract = True

    Teacher_id = models.CharField(max_length=32, primary_key=True)
    Class_id = models.ManyToManyField('classes.Classes', blank=True)
    #Student_id = models.ManyToManyField('student.Student', blank=True)


    def __str__(self):
        return self.Teacher_id