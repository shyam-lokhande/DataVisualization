from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
def home_view(req):
    return render(req,'home.html',{})

def login_view(req):
    err_msg=None
    form=LoginForm()
    if req.method=='POST':
        form=LoginForm(data=req.POST)
        if form.is_valid():
            username=form.data.get('username')
            password=form.data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(req,user)
                if req.GET.get('next'):
                    return redirect(req.GET.get('next'))
                else:
                    return redirect('home')
            else:
                err_msg="Something went wrong!"

    context={
        'form':form,
        'err_msg':err_msg
    }
    return render(req,'login.html',context)

def logout_view(request):
    logout(request)
    return render(request,'home.html')