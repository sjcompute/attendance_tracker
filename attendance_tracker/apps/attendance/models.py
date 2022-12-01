from django.db import models

class Attendance(models.Model):
    attendance_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Excused', 'Excused')
    ]
    
    
    date = models.DateField(null=True, auto_now_add=True)
    state = models.CharField(max_length=8, choices=attendance_choices, default='Present')
    student_id = models.ForeignKey('student.Student', blank=True, on_delete=models.PROTECT)
    class_id = models.ForeignKey('classes.Classes', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.state} {self.date} {self.class_id}'

    def save(self, *args, **kwargs):
        # Importing here to avoid circular import errors
        from apps.student.models import Student
        from apps.classes.models import Classes
        super(Attendance, self).save(*args, **kwargs)
        student = Student.objects.get(student_id = self.student_id)
        class_object = Classes.objects.get(class_id = self.class_id)
        class_object.state.add(self)
        student.state.add(self)
            