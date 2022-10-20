
from django.apps import apps
from django.db import models

#from apps.teacher.models import Teacher
#from apps.classes.models import Classes
# Create your models here.
class School(models.Model):
    #class Meta:
    #   abstract = True
    School_id = models.CharField(max_length=32, primary_key=True)
    Teacher_id = models.ManyToManyField('teacher.Teacher', blank=True)
    Class_id = models.ManyToManyField('classes.Classes', blank=True)
    Student_id = models.ManyToManyField('student.Student', blank=True)

    #x = Teacher.objects.filter(School_id=self.School_id)
    def save(self, *args, **kwargs):
        print(self)
        School_id = self.School_id
        print(School_id)
        x = School.objects.get(School_id=self.School_id)
        #School.objects.filter(School_id=self.School_id).add(Teacher_id = self.Teacher_id)
        print('this is x')
        print(x)
        x.add(Teacher_id = self.Teacher_id)
        super(School, x).save(*args, **kwargs)
    
    def __str__(self):
        return self.School_id
    

    
