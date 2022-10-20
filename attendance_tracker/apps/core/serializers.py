from rest_framework import serializers

from apps.school.models import School

class SchoolSerializer(serializers.ModelSerializer):
   class Meta:
       model = School
       fields = ('School_id', 'Teacher_id', 'Student_id', 'Class_id',)


#class SpeciesSerializer(serializers.ModelSerializer):
   #class Meta:
       #model = Species
       #fields = ('name', 'classification', 'language')