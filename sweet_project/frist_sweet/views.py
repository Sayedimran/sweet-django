from django.shortcuts import render
from django.http import HttpResponse
from . models import Customars, info
from . forms import customarRegistration
# Create your views here.
from django.http import HttpResponseRedirect

def big_data(request):
    return render(request,'frist_sweet.ai/big_data.html')


def  customar_info(request):
    cdatails = Customars.objects.all()
    return render(request, 'frist_sweet.ai/cts.html', {'cts':cdatails})

def user_form(request):
    if request.method == 'POST': 
       frm = customarRegistration(request.POST)
       if frm.is_valid():
        
           fname = frm.cleaned_data['frist_name']
           lname =frm.cleaned_data['last_name']
           eml = frm.cleaned_data['email']
           pnm = frm.cleaned_data['phone_number']
           txt = frm.cleaned_data['text_aria']
           passs = frm.cleaned_data['password']
           repass = frm.cleaned_data['re_password']
           pmt =  frm.cleaned_data['payment']
           chk = frm.cleaned_data['checkedbox']
           seor = frm.cleaned_data['make_seor']
           djangothree = info(frist_name=fname, last_name=lname, email=eml, phone_number=pnm, text_aria=txt, password=passs, re_password=repass, checkedbox=chk, payment=pmt, make_seor=seor)
           djangothree.save()
           return HttpResponseRedirect('/successfully/') 
           
       
    else:
        frm = customarRegistration()   
        print(' kfsm')
    return render(request,'frist_sweet.ai/forms.html', {'form':frm})

def sucsess(request):
    return render(request,'frist_sweet.ai/submit.html')