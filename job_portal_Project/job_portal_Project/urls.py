from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job_portal_Project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinPage,name="signinPage"),
    path('signupPage/',signupPage,name="signupPage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    path('joblistPage/',joblistPage,name="joblistPage"),

    #recruiter
    path('addjobPage/',addjobPage,name="addjobPage"),
    path('deletejob/<str:jobid>',deletejob,name="deletejob"),
    path('editjob/<str:jobid>',editjob,name="editjob"),
    path('viewjob/<str:jobid>',viewjob,name="viewjob"),


    path('profilePage/',profilePage,name="profilePage"),
    path('profileinfoPage/',profileinfoPage,name="profileinfoPage"),


    path('recruiterinfo/',recruiterinfo,name="recruiterinfo"),
    path('postedjob/',postedjob,name="postedjob"),
    path('applicant/<str:jobid>',applicant,name="applicant"),
    path('jobreject/<str:jobid>',jobreject,name="jobreject"),
    path('approved/<str:jobid>',approved,name="approved"),



    path('seekerinfo/',seekerinfo,name="seekerinfo"),
    path('applyjob/<str:jobid>',applyjob,name="applyjob"),
    path('appliedjob/',appliedjob,name="appliedjob"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
