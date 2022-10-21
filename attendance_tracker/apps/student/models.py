from django.db import models
from django.apps import apps



# Create your models here.

class Student(models.Model):    
        
    Student_id = models.CharField(max_length=32, primary_key=True)
    First_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)
    State = models.ManyToManyField('attendance.Attendance')
    Date = models.ManyToManyField('attendance.Attendance')


    def __str__(self):
        return f'{self.Student_id} {self.First_name} {self.Last_name}'
        #return self.Student_id + ' ' +  self.First_name + ' ' + self.Last_name
        

    
