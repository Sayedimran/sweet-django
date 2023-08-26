from django.contrib import admin
from . models import Customars, info


# Register your models here.
class CustomarAdmin(admin.ModelAdmin):
    list_display = ('id','customar_id','customar_name','customar_email','payment','product')
admin.site.register(Customars, CustomarAdmin)



class InfoAdmin(admin.ModelAdmin):
    list_display=('frist_name','last_name','email','phone_number','text_aria','password','re_password','checkedbox','payment','make_seor')




admin.site.register(info, InfoAdmin)