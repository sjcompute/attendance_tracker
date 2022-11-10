from django.db import models
from django.apps import apps


from apps.teacher.models import Teacher

class Classes(models.Model):
    Class_id = models.CharField(max_length=32, primary_key=True)
    Teacher_id = models.ForeignKey('teacher.Teacher', on_delete=models.PROTECT)
    Student_id = models.ManyToManyField('student.Student', blank=True)
    State = models.ManyToManyField('attendance.Attendance', blank=True)
   
    def __str__(self):
        return self.Class_id
    
    def save(self, *args, **kwargs):
        # Importing here to avoid circular import errors
        from apps.student.models import Student
        try:
            old_teacher = self.__class__._default_manager.filter(pk=self.pk).values('Teacher_id').get()['Teacher_id']
        except:
            pass
        super(Classes, self).save(*args, **kwargs)
        
        try:
            if self.Teacher_id != old_teacher:
                Teacher.objects.get(Teacher_id = old_teacher).Class_id.remove(self.Class_id)
                
        except:
            pass
        print(self.Student_id.all())
        for student_object in self.Student_id.all():
            student = Student.objects.get(Student_id = student_object.Student_id)
            student.Class_id.add(self.Class_id)
        teacher = Teacher.objects.get(Teacher_id = self.Teacher_id)
        teacher.Class_id.add(self.Class_id)
        
        

