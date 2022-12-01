from django.db import models
from django.db import transaction
from django.apps import apps


from apps.teacher.models import Teacher

class Classes(models.Model):
    class_id = models.CharField(max_length=32, primary_key=True)
    teacher_id = models.ForeignKey('teacher.Teacher', on_delete=models.PROTECT)
    student_id = models.ManyToManyField('student.Student', blank=True, symmetrical=False)
    state = models.ManyToManyField('attendance.Attendance', blank=True)
   
    def __str__(self):
        return self.class_id
    
    def save(self, *args, **kwargs):
        # Importing here to avoid circular import errors 
        try:
            old_teacher = self.__class__._default_manager.filter(pk=self.pk).values('teacher_id').get()['teacher_id']
        except:
            pass
        super(Classes, self).save(*args, **kwargs)
        try:
            if self.teacher_id != old_teacher:
                Teacher.objects.get(teacher_id = old_teacher).class_id.remove(self.class_id)
        except:
            pass
        print(self.student_id.all())
        teacher = Teacher.objects.get(teacher_id = self.teacher_id)
        teacher.class_id.add(self.class_id)
        transaction.on_commit(
            lambda: update_class(self) 
        )
        
def update_class(instance):
    from apps.student.models import Student
    for student_object in instance.student_id.all():
        student = Student.objects.get(student_id = student_object.student_id)
        student.class_id.add(instance.class_id)
        
        

