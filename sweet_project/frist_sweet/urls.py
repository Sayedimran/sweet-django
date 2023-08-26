from django.urls import path
from . import views 

urlpatterns = [
    path('',views.big_data,name="home" ),
    path('c/',views.customar_info,name="customar" ),
    path('form/',views.user_form,name=" sform" ),
    path('successfully/',views.sucsess, name='successfully' ),
    
]