from django.shortcuts import render,redirect
from job_portal_App.models import *
from job_portal_Project.forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


def signupPage(request):
    if request.method=='POST':
        signup=signup_form(request.POST, request.FILES)
        if signup.is_valid():
            signup.save()
            return redirect('signinPage')
    else:
        signup=signup_form()
    return render(request,'common/signupPage.html',{'signup':signup})


def signinPage(request):
    if request.method=='POST':
        signin=signin_form(request,data=request.POST)
        if signin.is_valid():
            user=signin.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        signin=signin_form()
    return render(request,'common/signinPage.html',{'signin':signin})


@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('signinPage')