from django import forms 
from django.core import validators


class customarRegistration(forms.Form):
    frist_name = forms.CharField(error_messages={'required':'Enter your name must'})
    last_name = forms.CharField(label='Enter Last Name')
    email = forms.EmailField(validators=[validators.MaxLengthValidator(20)]) 
    phone_number = forms.IntegerField(widget=forms.NumberInput())

    text_aria     = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'col':15}))
    password    = forms.CharField(widget=forms.PasswordInput(),min_length=6 ,max_length=15) 
    re_password = forms.CharField(widget=forms.PasswordInput(),min_length=6 ,max_length=15)   
    checkedbox = forms.CharField(widget=forms.CheckboxInput(), )
    payment    = forms.DecimalField(min_value=250, max_value=4000,max_digits=6,decimal_places=2)
    make_seor = forms.BooleanField()


    def clean(self):
        cleaned_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if  password_match != re_password_match:
              raise forms.ValidationError('password does not match')
                 
