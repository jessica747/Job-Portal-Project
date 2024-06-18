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

@login_required
def addjobPage(request):
    if request.method =='POST':
        print("i am in the post method now")
        addjobform=add_job_form(request.POST)
        if addjobform.is_valid():
            user=addjobform.save(commit=False)
            user.adduser=request.user
            addjobform.save()
            return redirect('joblistPage')
    else:
        print("i am in else now")
        addjobform=add_job_form()   

    return render(request,'recruiter/addjobPage.html',{'addjobform':addjobform})


@login_required
def joblistPage(request):
    jobdata=add_job_model.objects.all()
    return render(request,'common/joblistPage.html',{'jobdata':jobdata})

@login_required
def deletejob(request,jobid):
    deletedata=add_job_model.objects.get(id=jobid)
    deletedata.delete()
    return redirect('joblistPage')

@login_required
def editjob(request,jobid):
    editjobdata=add_job_model.objects.get(id=jobid)
    if request.method=='POST':
        editjobdataform=add_job_form(request.POST,instance=editjobdata)
        if editjobdataform.is_valid():
            editjobdataform.save()
            return redirect('joblistPage')
    else:
        editjobdataform=add_job_form(instance=editjobdata)
    return render(request,'recruiter/editjob.html',{'editjobdataform':editjobdataform})


@login_required
def viewjob(request,jobid):
    viewjobdata=add_job_model.objects.get(id=jobid)
    return render(request,'common/viewjob.html',{'viewjobdata':viewjobdata})


@login_required
def profilePage(request):
    return render(request,'profile/profilePage.html')

@login_required
def profileinfoPage(request):
    return render(request,'profile/profileinfoPage.html')


@login_required
def recruiterinfo(request):
    recdadainfo=recruiter_info_model.objects.all()
    return render(request,'profile/recruiterinfo.html',{'recdadainfo': recdadainfo})


@login_required
def seekerinfo(request):
    seekerdadainfo=seeker_info_model.objects.all()
    return render(request,'profile/seekerinfo.html',{'seekerdadainfo': seekerdadainfo})


@login_required
def postedjob(request):
    current_user=request.user
    if current_user.user_type == 'recruiter':
        posteddata=add_job_model.objects.filter(adduser=current_user)
    return render(request,'recruiter/postedjob.html',{'posteddata':posteddata})


@login_required
def applyjob(request,jobid):
    job=add_job_model.objects.get(id=jobid)
    if request.method=='POST':
        applyjobdata=apply_job_form(request.POST,request.FILES)
        if applyjobdata.is_valid():
            jobdata=applyjobdata.save(commit=False)
            jobdata.applicant=request.user
            jobdata.applied_job=job
            jobdata.save()
            return redirect('joblistPage')
    else:
        applyjobdata=apply_job_form()
    return render(request,'seeker/applyjob.html',{'applyjobdata':applyjobdata})

@login_required
def appliedjob(request):
    current_user=request.user
    applieddata=apply_job_model.objects.filter(applicant=current_user)

    return render(request,'seeker/appliedjob.html',{'applieddata':applieddata})

@login_required
def applicant(request,jobid):
    job=add_job_model.objects.get(id=jobid)
    applicantdata=apply_job_model.objects.filter(applied_job=job)
    return render(request,'recruiter/applicant.html',{'applicantdata':applicantdata})


@login_required
def jobreject(request,jobid):
    jobrejectinfo=apply_job_model.objects.get(id=jobid)
    jobrejectinfo.status="Rejected"
    jobrejectinfo.save()
    
    return redirect('postedjob')

@login_required
def approved(request,jobid):
    approveddata=apply_job_model.objects.get(id=jobid)
    approveddata.status="Approved"
    approveddata.save()
    
    return redirect('postedjob')

