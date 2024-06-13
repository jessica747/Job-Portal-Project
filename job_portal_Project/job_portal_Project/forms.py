from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from job_portal_App.models import *

class signup_form(UserCreationForm):
    class Meta:
        model = custom_user_model
        fields = UserCreationForm.Meta.fields+('username',
        'user_type','display_name','profile_picture','email',)


class signin_form(AuthenticationForm):
    class Meta:
        models =custom_user_model
        fields = ('username','password')
    
        
        