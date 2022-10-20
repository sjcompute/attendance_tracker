from django.db import models
from django.apps import apps

# Create your models here.

class Student(models.Model):
    #class Meta:
    #    abstract = True
        
    Student_id = models.CharField(max_length=32, primary_key=True)
    School_id = models.ForeignKey('school.School', on_delete=models.PROTECT)
    Teacher_id = models.ManyToManyField('teacher.Teacher', blank=True)
    Class_id = models.ManyToManyField('classes.Classes', blank=True)
    First_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)


    def __str__(self):
        return self.Student_id + ' ' +  self.First_name + ' ' + self.Last_name
    


