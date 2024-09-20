from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('elements',views.elements,name='elements'),
    path('job_details/<int:job_id>/',views.job_details,name='job_details'),
    path('job_listing',views.job_listing,name='job_listing'),
    path('singleblog',views.singleblog,name='singleblog'),
    path('signup',views.signup,name='signup'),
    path('otp',views.otp,name='otp'),
    path('login',views.login,name='login'),
    path('verifyotp',views.verifyotp,name='verifyotp'),
    path('logout',views.logout,name='logout'),
    path('change_password',views.change_password,name='change_password'),


    path('PostAJOb',views.PostAJob,name='PostAJob'),



    path('job_application',views.job_application,name='job_application'),
    path('employer_profile',views.employer_profile,name='employer_profile'),
    path('editemployer_profile',views.editemployer_profile,name='editemployer_profile'),
    path('emrdetails',views.emrdetails,name='emrdetails'),
    path('employer_image_logo',views.employer_image_logo,name='employer_image_logo'),
    path('employer_PostAJob',views.employer_PostAJob,name='employer_PostAJob'),
    path('delete_job/<emp_id>',views.delete_job,name='delete_job'),

    path('jobseeker_profile',views.jobseeker_profile,name='jobseeker_profile'),
    path('jobseeker_details',views.jobseeker_details,name='jobseeker_details'),

    path('Edit_jobseeker_profile',views.Edit_jobseeker_profile,name='Edit_jobseeker_profile'),
    path('Edit_jobseeker_image_resume',views.Edit_jobseeker_image_resume,name='Edit_jobseeker_image_resume'),
    path('apply_job/<empye_id>',views.apply_job,name='apply_job'),
    path('employer_dashboard/<int:job_id>/',views.employer_dashboard,name='employer_dashboard'),
    path('post_job_list',views.post_job_list,name='post_job_list'),
    path('job_accept/<j_id>',views.job_accept,name='job_accept'),
    path('job_reject/<r_id>',views.job_reject,name='job_reject'),







   







    

    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
