

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm




class ucfrm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name']
    