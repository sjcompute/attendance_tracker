from django.apps import apps
from django.db import models

#from apps.classes.models import Classes
from apps.school.models import School
# Create your models here.
class Teacher(models.Model):
    #class Meta:
    #   abstract = True

    Teacher_id = models.CharField(max_length=32, primary_key=True)
    School_id = models.ForeignKey('school.School', on_delete=models.PROTECT)
    Class_id = models.ManyToManyField('classes.Classes', blank=True)
    Student_id = models.ManyToManyField('student.Student', blank=True)


    def __str__(self):
        return self.Teacher_id
    
    def save(self, *args, **kwargs):
        try:
            school_type = School.objects.get(
                School_id=self.School_id,)
            #print(school_type)
            if School.objects.get(School_id=self.School_id):
                try:
                    if School.objects.get(Teacher_id=self.Teacher_id):
                        print("getting somewhere")
                except:
                    #b2 = School.create_teacher(Teacher_id=self.Teacher_id)

                    School.save(self=self)
                    print("getting somewhere maybe")
            #else:
                #print(School.objects.get())
                    
            if self.Teacher_id is None:
                #school_type.T = voucher_type.last_number+1
                #self.type = school_type
                school_type.save()
        except Exception as e:
            print (e)
        super(Teacher, self).save(*args, **kwargs)
    