from django.contrib import admin
from . models import customar , Student , Course

# Register your models here.
@admin.register(customar)
class custAdmin(admin.ModelAdmin):
    list_display = ['customar_name','customar_reg','user']



# Meny to one 
@admin.register(Student)
class stuAdmin(admin.ModelAdmin):
    list_display=['Student_name','Student_reg','total','user']



# many to many 
@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display= ['Course_name','Course_code','corse_teacher']