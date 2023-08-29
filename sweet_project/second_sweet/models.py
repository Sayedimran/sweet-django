from django.db import models
from django.contrib.auth.models import User  
# Create your models here.



# one to one relationship 
class customar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customar_name = models.CharField(max_length=30)
    customar_reg = models.IntegerField()


# Many To One 
class  Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    Student_name = models.CharField(max_length=20)
    Student_reg = models.IntegerField()
    total = models.CharField(max_length=20)
    
# Many To many
class Course(models.Model):
    user = models.ManyToManyField(User)
    Course_name = models.CharField(max_length=25)
    Course_code = models.IntegerField()
    

    def corse_teacher(self):
        return ",".join([str(p) for p in self.user.all()])





