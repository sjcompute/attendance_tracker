from django.db import models
from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver
import time


from django.utils.text import slugify
class Student(models.Model):    
        
    Student_id = models.CharField(max_length=32, primary_key=True)
    First_name = models.CharField(max_length=32)
    Last_name = models.CharField(max_length=32)
    Class_id = models.ManyToManyField('classes.Classes', blank=True)
    State = models.ManyToManyField('attendance.Attendance', related_name='states', blank=True)
    #Date = models.ManyToManyField('attendance.Attendance', related_name='dates', blank=True)


    def __str__(self):
         #return self.Student_id
        return f'{self.Student_id}'


    def save(self, *args, **kwargs):
        from apps.classes.models import Classes # Importing here to avoid circular import errors
        super(Student, self).save(*args, **kwargs)
        for course in self.Class_id.all():
            course_object = Classes.objects.get(Class_id=course.Class_id)
            course_object.Student_id.add(self)
            

@receiver(models.signals.post_save, sender=Student)
def test(sender, instance, created, **kwargs):
    student = instance.Student_id
    print(Student.objects.get(Student_id=student).Class_id.all())
    print(sender)
    print(created)
    
        
            
            
  
        
        
        

    
