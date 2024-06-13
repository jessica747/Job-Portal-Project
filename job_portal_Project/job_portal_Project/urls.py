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




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
