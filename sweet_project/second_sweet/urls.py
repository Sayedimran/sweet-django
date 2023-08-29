from django.urls import path

from . import views 

urlpatterns = [
   
    
    path('ft/',views.free_tools,name="sew" ),

    path('sw/',views.fr_swet,name="sewt" ),

    path('ucfrm/',views.usercform,name='regitrations'),

    path('login/',views.login_form, name='login' ),
    
    path('succsess/',views.slogin),

    path('logout/',views.logout_form , name="logout" ),
    path('passc/',views.password_change, name="passwordchnage") ,
    
    path('withOutoldpass/',views.without_old_pass, name="withoutOldPassword") ,
    
    path('classblack/',views.fristpro.as_view()),
    path('templteviw/',views.fristTempu.as_view()),
]