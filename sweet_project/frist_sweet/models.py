from django.db import models

# Create your models here.
class Customars(models.Model):
    customar_id = models.IntegerField()
    customar_name = models.CharField(max_length=50)
    customar_email = models.EmailField(max_length=30)
    payment = models.IntegerField()
    product = models.CharField(max_length=20)  






class info(models.Model):
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    phone_number = models.IntegerField()
    text_aria = models.CharField(max_length=300)
    password  = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    checkedbox =models.CharField(max_length=20)
    payment = models.DecimalField(max_digits=6,decimal_places=2)
    make_seor = models.BooleanField()

    
    
      