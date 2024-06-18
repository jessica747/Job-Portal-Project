from django.contrib import admin
from job_portal_App.models import *

class custom_user_model_display(admin.ModelAdmin):
    list_display=['username','user_type']

admin.site.register(custom_user_model,custom_user_model_display)
admin.site.register(recruiter_info_model)
admin.site.register(seeker_info_model)
admin.site.register(add_job_model)
admin.site.register(apply_job_model)