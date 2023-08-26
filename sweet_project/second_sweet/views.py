from django.shortcuts import render ,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from  . forms import ucfrm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm ,SetPasswordForm
from django.contrib.auth import  authenticate, login , logout , update_session_auth_hash




# Create your views here. 


def free_tools(request):
    return render ( request,'second_sweet.ai/blog.html') 

def fr_swet(request):
    return render ( request,'second_sweet.ai/ecom.html') 

# Registrations 
def usercform(request):
    if request.method == "POST":
        fm = ucfrm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = ucfrm()   
       
    
    return render (request, 'second_sweet.ai/usercform.html', {'form': fm })


#Login 

def  login_form(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            user =  authenticate(username = uname, password = upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect ('/si/succsess')
    else:
      frm = AuthenticationForm()
    return render( request, 'second_sweet.ai/login.html', {'form':frm} )

def slogin(request):
    return render (request,'second_sweet.ai/succsess.html')



# logout 
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/si/succsess/')


# passwordchange 
def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = PasswordChangeForm(user = request.user , data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/si/succsess')
        else:     
            frm = PasswordChangeForm(user = request.user )
        return render (request, 'second_sweet.ai/passc.html', {'form':frm})
    
    else:
        return HttpResponseRedirect('/si/login')


#   without old pass 
def  without_old_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = PasswordChangeForm(user = request.user , data = request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/si/succsess')
        else:     
            frm = SetPasswordForm(user = request.user )
        return render (request, 'second_sweet.ai/withoutpassc.html', {'form':frm})
    
    else:
        return HttpResponseRedirect('/si/login')