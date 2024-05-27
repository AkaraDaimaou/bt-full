from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    teachers = models.ManyToManyField('Teacher', related_name='courses') #string reference

    def __str__(self):
        return self.course_name
        
class SchoolFacility(models.Model):
    facility_name = models.CharField(max_length=100)
    usage_purpose = models.TextField()
            
    def __str__(self):
        return self.facility_name
            
class Laboratory(models.Model):
                equipment_list = models.TextField()

                def __str__(self):
                    return f"{self.facility_name} - Laboratory"
                
