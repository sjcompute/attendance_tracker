from django.db import models


# Create your models here.

class Attendance(models.Model):
    Date = models.DateField(null=True, auto_now_add=True)
    State = models.BooleanField(blank=True)
    Student_id = models.ManyToManyField('student.Student', blank=True)
    Class_id = models.ForeignKey('classes.Classes', null=True, blank=True, on_delete=models.PROTECT)