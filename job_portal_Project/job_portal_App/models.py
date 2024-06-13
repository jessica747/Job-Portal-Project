from django.db import models
from django.contrib.auth.models import AbstractUser

class custom_user_model(AbstractUser):
    Usertype=[
        ('recruiter','Recruiter'),
        ('jobseeker','jobseeker'),
    ]

    user_type=models.CharField(choices=Usertype,max_length=100,null=True)
    display_name=models.CharField(max_length=100,null=True)
    profile_picture=models.ImageField(upload_to='media/profilephoto',null=True)

class recruiter_info_model(models.Model):
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=200,null=True)
    company_description=models.TextField(null=True)
    recriteruser=models.OneToOneField(custom_user_model,on_delete=models.CASCADE,related_name='recruiter_info',null=True)

    def __str__(self):
        return self.company_name
    

class seeker_info_model(models.Model):
    skill_set=models.CharField(max_length=100,null=True)
    resume=models.FileField(upload_to='media/seekerresume',null=True)
    seekeruser=models.OneToOneField(custom_user_model,on_delete=models.CASCADE,related_name='seeker_info',null=True)

    def __str__(self):
        return self.skill_set
    

class add_job_model(models.Model):
    title=models.CharField(max_length=100,null=True)
    number_of_openings=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    skills_set=models.CharField(max_length=100,null=True)
    job_description=models.TextField(null=True)

    adduser=models.ForeignKey(custom_user_model,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


