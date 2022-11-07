from django.db import models
from apps.student.models import Student


# Create your models here.

class Attendance(models.Model):
    attendance_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Excused', 'Excused')
    ]
    
    
    Attendance_id = models.AutoField(primary_key=True)
    Date = models.DateField(null=True, auto_now_add=True)
    State = models.CharField(max_length=8, choices=attendance_choices, default='Present')
    Student_id = models.ForeignKey('student.Student', blank=True, on_delete=models.PROTECT)
    Class_id = models.ForeignKey('classes.Classes', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.State} {self.Date} {self.Class_id}'

    def save(self, *args, **kwargs):
        super(Attendance, self).save(*args, **kwargs)
        student = Student.objects.get(Student_id = self.Student_id)
        student.State.add(self)
            