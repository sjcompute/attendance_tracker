from django.db import models
from django.apps import apps



# Create your models here.

class Student(models.Model):    
        
    Student_id = models.CharField(max_length=32, primary_key=True)
    First_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)
    Class_id = models.ManyToManyField('classes.Classes', blank=True)
    State = models.ManyToManyField('attendance.Attendance', related_name='states', blank=True)
    #Date = models.ManyToManyField('attendance.Attendance', related_name='dates', blank=True)


    def __str__(self):
         return self.Student_id
    #     #return self.Student_id + ' ' +  self.First_name + ' ' + self.Last_name
    
    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        

    
