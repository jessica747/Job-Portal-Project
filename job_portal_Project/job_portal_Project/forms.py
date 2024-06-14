from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from job_portal_App.models import *
from django import forms

class signup_form(UserCreationForm):
    class Meta:
        model = custom_user_model
        fields = UserCreationForm.Meta.fields+('username',
        'user_type','display_name','profile_picture','email',)


class signin_form(AuthenticationForm):
    class Meta:
        models =custom_user_model
        fields = ('username','password')

class add_job_form(forms.ModelForm):
    class Meta:
        model=add_job_model
        fields= ['title','number_of_openings','category','skills_set','job_description']
    
        
        