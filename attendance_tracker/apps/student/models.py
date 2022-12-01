from django.db import models
from django.db import transaction


from django.utils.text import slugify
class Student(models.Model):    
        
    student_id = models.CharField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    class_id = models.ManyToManyField('classes.Classes', blank=True, symmetrical=False)
    state = models.ManyToManyField('attendance.Attendance', related_name='states', blank=True)
    #date= models.ManyToManyField('attendance.Attendance', related_name='dates', blank=True)


    def __str__(self):
         #return self.student_id
        return f'{self.student_id}'


    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        transaction.on_commit(
        lambda: update_student(self))
  
  
def update_student(instance):
    from apps.classes.models import Classes # Importing here to avoid circular import errors
    print(instance.class_id.all())
    for course in instance.class_id.all():
        course_object = Classes.objects.get(class_id=course.class_id)
        course_object.student_id.add(instance)

    
        
            
            
  
        
        
        

    
