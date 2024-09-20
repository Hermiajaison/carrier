from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
<<<<<<< HEAD
=======
    path('admin/', admin.site.urls),
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
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
<<<<<<< HEAD
=======
    path('dash_about',views.dash_about,name='dash_about'),
    path('purchase',views.purchase,name='purchase'),


>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
    path('change_password',views.change_password,name='change_password'),


    path('PostAJOb',views.PostAJob,name='PostAJob'),



    path('job_application',views.job_application,name='job_application'),
    path('employer_profile',views.employer_profile,name='employer_profile'),
    path('editemployer_profile',views.editemployer_profile,name='editemployer_profile'),
    path('emrdetails',views.emrdetails,name='emrdetails'),
    path('employer_image_logo',views.employer_image_logo,name='employer_image_logo'),
    path('employer_PostAJob',views.employer_PostAJob,name='employer_PostAJob'),
    path('delete_job/<emp_id>',views.delete_job,name='delete_job'),

<<<<<<< HEAD
=======
    path('edit_jobdetails/<int:job_id>/',views.edit_jobdetails,name='edit_jobdetails'),


>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
    path('jobseeker_profile',views.jobseeker_profile,name='jobseeker_profile'),
    path('jobseeker_details',views.jobseeker_details,name='jobseeker_details'),

    path('Edit_jobseeker_profile',views.Edit_jobseeker_profile,name='Edit_jobseeker_profile'),
    path('Edit_jobseeker_image_resume',views.Edit_jobseeker_image_resume,name='Edit_jobseeker_image_resume'),
    path('apply_job/<empye_id>',views.apply_job,name='apply_job'),
    path('employer_dashboard/<int:job_id>/',views.employer_dashboard,name='employer_dashboard'),
    path('post_job_list',views.post_job_list,name='post_job_list'),
    path('job_accept/<j_id>',views.job_accept,name='job_accept'),
    path('job_reject/<r_id>',views.job_reject,name='job_reject'),

<<<<<<< HEAD






   
=======
    path('accepted_applications',views.accepted_applications,name='accepted_applications'),
    path('rejected_applications',views.rejected_applications,name='rejected_applications'),

    path('jobseeker_activity',views.jobseeker_activity,name='jobseeker_activity'),
    path('jobseeker_successjobs',views.jobseeker_successjobs,name='jobseeker_successjobs'),
    path('jobseeker_failurejobs',views.jobseeker_failurejobs,name='jobseeker_failurejobs'),

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('jobseeker_dashboard',views.jobseeker_dashboard,name='jobseeker_dashboard'),
    path('alljobs_dashboard',views.alljobs_dashboard,name='alljobs_dashboard'),
    path('analitycs',views.analitycs,name='analitycs'),
    path('sendmessage',views.sendmessage,name='sendmessage'),
    path('employer_delete/<data_id>/',views.employer_delete,name='employer_delete'),
    path('jobseeker_delete/<da_id>/',views.jobseeker_delete,name='jobseeker_delete'),
    path('dashdel_job/<int:data_id>/',views.dashdel_job,name='dashdel_job'),



    path('job_search',views.job_search,name='job_search'),
    path('search',views.search,name='search'),
    path('news',views.news,name='news'),

    path('changepassword',views.changepassword,name='changepassword'),

    path('jobseekerProfilePasswordUpdate',views.jobseekerProfilePasswordUpdate, name='jobseekerProfilePasswordUpdate'),
    path('admin_employerProfile/<int:empr_id>/',views.admin_employerProfile, name='admin_employerProfile'),
    path('Admin_Employeraccept/<int:j_id>/', views.Admin_Employeraccept, name='Admin_Employeraccept'),

    path('admin_jobseekerProfile/<int:empe_id>/',views.admin_jobseekerProfile, name='admin_jobseekerProfile'),
    path('Admin_jobseekeraccept/<int:j_id>/', views.Admin_jobseekeraccept, name='Admin_jobseekeraccept'),

    path('admin_AlljobsDetails/<int:jo_id>/', views.admin_AlljobsDetails, name='admin_AlljobsDetails'),
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4







<<<<<<< HEAD
    

    
=======








    path('video',views.video),


>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
