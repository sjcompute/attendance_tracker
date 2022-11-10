from django.db import models

class Attendance(models.Model):
    attendance_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Excused', 'Excused')
    ]
    
    
    Date = models.DateField(null=True, auto_now_add=True)
    State = models.CharField(max_length=8, choices=attendance_choices, default='Present')
    Student_id = models.ForeignKey('student.Student', blank=True, on_delete=models.PROTECT)
    Class_id = models.ForeignKey('classes.Classes', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.State} {self.Date} {self.Class_id}'

    def save(self, *args, **kwargs):
        # Importing here to avoid circular import errors
        from apps.student.models import Student
        from apps.classes.models import Classes
        super(Attendance, self).save(*args, **kwargs)
        student = Student.objects.get(Student_id = self.Student_id)
        class_object = Classes.objects.get(Class_id = self.Class_id)
        class_object.State.add(self)
        student.State.add(self)
            