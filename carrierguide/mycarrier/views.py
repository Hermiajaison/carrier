import random
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
<<<<<<< HEAD
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
=======
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.hashers import check_password, make_password
from twilio.rest import Client

>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4








def index(request):
    try:
        EMAIL=request.session['EMAIL']
        emp=User_employer.objects.get(EMAIL=EMAIL)
        
        data = EMPLOYER_post_a_job.objects.filter(DETAILS_OF_COMPANY=emp)


        context = {
            'data': data,
<<<<<<< HEAD
=======
            'emp':emp
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4


        
        }
        return render(request, 'index.html',context)
    except:

        data = EMPLOYER_post_a_job.objects.all()
    

        context = {
            'data': data,

        
        }
        return render(request, 'index.html',context)




    

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')

<<<<<<< HEAD
=======
def purchase(request):
    return render(request, 'purchase.html')

>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4




def job_details(request,job_id):
<<<<<<< HEAD

    
    job = EMPLOYER_post_a_job.objects.get(id=job_id)
   

    context = {
        'job': job
=======
    EMAIL = request.session.get('EMAIL')
    
    job = EMPLOYER_post_a_job.objects.get(id=job_id)
    job_status=jobseeker_apply_job.objects.filter(user=EMAIL,DETAILS_OF_JOB=job)
    if jobseeker_apply_job.objects.filter(user=EMAIL,DETAILS_OF_JOB=job).exists():
        job_status=True
    else:
        job_status=False
   

    print(job_status,'/////////////////////////////////////')
    context = {
        'job': job,
        'job_status':job_status
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4

       
    }
    return render(request, 'job_details.html',context)



<<<<<<< HEAD
=======






>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
def job_listing(request):
    data = EMPLOYER_post_a_job.objects.all()
   

    context = {
        'data': data

       
    }
    return render(request, 'job_listing.html',context)

def singleblog(request):
    return render(request, 'single-blog.html')

def signup(request):
    return render(request, 'signup.html')

def otp(request):
    if request.method == 'POST':
        msg=None
        USERNAME = request.POST['name']
        EMAIL = request.POST['email']
        PASSWORD = request.POST['password']
        USERTYPE = request.POST.get('usertype')


        if User_employer.objects.filter(EMAIL=EMAIL).exists():
            print("USER ALREADY EXISTS")
            messages.error(request,"USER ALREADY EXISTS PLEASE LOGIN")
            return redirect('login')

        elif User_jobseeker.objects.filter(EMAIL=EMAIL).exists():
            print("USER ALREADY EXISTS")
            messages.error(request,"USER ALREADY EXISTS PLEASE LOGIN")


            return redirect('login')

        random_number = random.randint(1000, 9999)

        SUBJECT = 'Email'
        MESSAGE = f'Your OTP for carrierguide is {random_number}'

        send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)

<<<<<<< HEAD
=======
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            from_= settings.TWILIO_PHONE_NUMBER,
            body= f'Your OTP for carrierguide is {random_number}',
            to='+918139871762')



>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
        request.session['EMAIL'] = EMAIL
        request.session['PASSWORD'] = PASSWORD
        request.session['USERNAME'] = USERNAME
        request.session['USERTYPE'] = USERTYPE
        request.session['random_number'] = random_number  # Save the random number to session

        print(USERNAME, EMAIL, PASSWORD, USERTYPE, random_number)

        return render(request, 'otp.html')
    return render(request, 'otp.html')

def verifyotp(request):
    random_number = request.session.get('random_number')  # Get the random number from session
    if request.method == 'POST':
        f1 = str(request.POST['otp1'])
        f2 = str(request.POST['otp2'])
        f3 = str(request.POST['otp3'])
        f4 = str(request.POST['otp4'])

        user_otp = f1 + f2 + f3 + f4
        print(user_otp)

        if int(user_otp) == int(random_number):
            print("SUCCESSFUL")

            USERNAME = request.session.get('USERNAME')
            EMAIL = request.session.get('EMAIL')
            PASSWORD = request.session.get('PASSWORD')
            USERTYPE = request.session.get('USERTYPE')
            if USERTYPE=='Employer':
               
                newuser = User_employer(USERNAME=USERNAME, EMAIL=EMAIL, PASSWORD=PASSWORD)
                newuser.save()

            else:
                user = User_jobseeker(USERNAME=USERNAME, EMAIL=EMAIL, PASSWORD=PASSWORD)
                user.save()


        

            del request.session['EMAIL']
            del request.session['PASSWORD']
            del request.session['USERNAME']
            del request.session['USERTYPE']
            del request.session['random_number']

            return render(request, 'login.html')
        
        return render(request, 'otp.html')
    
    return render(request, 'otp.html')








def login(request):
    if request.method == 'POST':
        EMAIL = request.POST['email']
        PASSWORD = request.POST['password']
        
        if User_employer.objects.filter(EMAIL=EMAIL,PASSWORD=PASSWORD).exists():
            request.session['is_logged_in'] = True
            request.session['EMAIL']=EMAIL
            request.session['user_type'] = 'employer'
            return redirect('index')
        
        elif User_jobseeker.objects.filter(EMAIL=EMAIL,PASSWORD=PASSWORD).exists():
            request.session['is_logged_in_em'] = True
            request.session['EMAIL']=EMAIL
            request.session['user_type'] = 'jobseeker'
            return redirect('index')
<<<<<<< HEAD
=======
        user_obj = authenticate(username=EMAIL, password=PASSWORD)

        if user_obj and user_obj.is_superuser:
            auth_login(request, user_obj)  # Log in the admin user
            return redirect(admin_dashboard) 
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
        else:
            messages.error(request,"Invalid email or password .Please Sign up")
            return redirect('signup')
        
<<<<<<< HEAD
        
        
=======
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
    return render(request,'login.html')

def change_password(request):
    return render(request, 'changepassword.html')


def logout(request):
    # Clear the session data
    request.session.flush()
    
    return redirect('index')

def job_application(request):
    return render(request, 'jobapplication.html')
def PostAJob(request):
    return render(request, 'PostAJob.html')
<<<<<<< HEAD
=======
def dash_about(request):
    return render(request, 'dashabout.html')
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4




def employer_PostAJob(request):
    EMAIL = request.session.get('EMAIL')
    codet=User_employer.objects.get(EMAIL=EMAIL)
    if request.method == 'POST':
        JOB_TITLE = request.POST.get('JOB_TITLE')
        JOB_POSITION = request.POST.get('JOB_POSITION')
        JOB_DESCRIPTION = request.POST.get('JOB_DESCRIPTION')
        JOB_STATE = request.POST.get('JOB_STATE')
        JOB_COUNTRY = request.POST.get('JOB_COUNTRY')
        JOB_LOCATION = request.POST.get('JOB_LOCATION')
        JOB_POSTED_DATE = request.POST.get('JOB_POSTED_DATE')
        JOB_APPLICATION_END_DATE = request.POST.get('JOB_APPLICATION_END_DATE')
        JOB_NATURE = request.POST.get('JOB_NATURE')
        JOB_EDUCATION_EXPERIENCE = request.POST.get('JOB_EDUCATION_EXPERIENCE')

        JOB_REQUIRED_KNOWLEDGE = request.POST.get('JOB_REQUIRED_KNOWLEDGE')
        JOB_NUMBER_OF_VACANCY = request.POST.get('JOB_NUMBER_OF_VACANCY')
        JOB_SALARY = request.POST.get('JOB_SALARY')

       
        job_user = EMPLOYER_post_a_job(JOB_TITLE=JOB_TITLE,
                                    JOB_POSITION=JOB_POSITION,
                                    JOB_DESCRIPTION=JOB_DESCRIPTION,
                                    JOB_STATE=JOB_STATE,
                                    JOB_COUNTRY=JOB_COUNTRY,
                                    JOB_LOCATION=JOB_LOCATION,
                                    JOB_POSTED_DATE=JOB_POSTED_DATE,
                                    JOB_APPLICATION_END_DATE=JOB_APPLICATION_END_DATE,
                                    JOB_NATURE=JOB_NATURE,
                                    JOB_EDUCATION_EXPERIENCE=JOB_EDUCATION_EXPERIENCE,
                                    JOB_REQUIRED_KNOWLEDGE=JOB_REQUIRED_KNOWLEDGE,
                                    JOB_NUMBER_OF_VACANCY=JOB_NUMBER_OF_VACANCY,
                                    JOB_SALARY=JOB_SALARY,
                                    DETAILS_OF_COMPANY=codet)
        job_user.save()

        return redirect(index)
        
    return render(request,'index.html')

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def employer_profile(request):
    
    EMAIL=request.session['EMAIL']
    
    employer=User_employer.objects.get(EMAIL=EMAIL)
    print(employer)
    # Pass the employer details to the template
    context = {
        'employer': employer
    }
    
    return render(request, 'employerprofile.html', context)

def editemployer_profile(request):
    EMAIL=request.session['EMAIL']
    employer=User_employer.objects.get(EMAIL=EMAIL)
    # Pass the employer details to the template
    context = {
        'employer': employer
    }
    return render(request, 'EditEmployerProfile.html',context)

def emrdetails(request):
    EMAIL = request.session.get('EMAIL')
    
    
    
    if request.method == 'POST':
        
        print('====----------===========-----------')
        print(EMAIL)
        EMPLOYER_NAME = request.POST.get('EMPLOYER_NAME')
        COMPANY_NAME = request.POST.get('COMPANY_NAME')
        EMPLOYER_LOCATION = request.POST.get('EMPLOYER_LOCATION')
        EMPLOYER_STATE = request.POST.get('EMPLOYER_STATE')
        EMPLOYER_PROFESSION = request.POST.get('EMPLOYER_PROFESSION')
        EMPLOYER_AGE = request.POST.get('EMPLOYER_AGE')
        EMPLOYER_JOB_NATURE = request.POST.get('EMPLOYER_JOB_NATURE')
        EMPLOYER_PHONE = request.POST.get('EMPLOYER_PHONE')
        
       
        
        # Update or create the employer record
        User_employer.objects.filter(
            EMAIL=EMAIL).update(EMPLOYER_NAME= EMPLOYER_NAME,
                COMPANY_NAME = COMPANY_NAME,
                EMPLOYER_LOCATION = EMPLOYER_LOCATION,
                EMPLOYER_STATE = EMPLOYER_STATE,
                EMPLOYER_PROFESSION = EMPLOYER_PROFESSION,
                EMPLOYER_AGE = EMPLOYER_AGE,
                EMPLOYER_JOB_NATURE = EMPLOYER_JOB_NATURE,
                EMPLOYER_PHONE = EMPLOYER_PHONE,
               
            
        )
        
        return redirect('employer_profile')

    
   

    return redirect('index')  


def employer_image_logo(request):
        EMAIL = request.session.get('EMAIL')
        if request.method == 'POST':
            EMPLOYER_IMAGE = request.FILES.get('EMPLOYER_IMAGE')
            COMPANY_LOGO = request.FILES.get('COMPANY_LOGO')
            newdata=User_employer.objects.get(EMAIL=EMAIL)

            if EMPLOYER_IMAGE !=None:
                newdata.EMPLOYER_IMAGE=EMPLOYER_IMAGE
            if COMPANY_LOGO !=None:   
                newdata.COMPANY_LOGO=COMPANY_LOGO

            newdata.save()
            return redirect('employer_profile')

        return redirect('index')


def delete_job(request,emp_id):
    print("job post delete")
    id = emp_id
    
    EMPLOYER_post_a_job.objects.filter(id=id).delete()

    return redirect('index')


<<<<<<< HEAD
=======
def edit_jobdetails(request,job_id):
    # Retrieve the job entry using job_id
    job =  EMPLOYER_post_a_job.objects.get(id=job_id)
    
    JOB_TITLE=request.session.get("JOB_TITLE")
    
    if request.method == 'POST':
        # Extracting updated job details from the POST request
        job_title = request.POST.get('JOB_TITLE')
        job_position = request.POST.get('JOB_POSITION')
        job_description = request.POST.get('JOB_DESCRIPTION')
        job_state = request.POST.get('JOB_STATE')
        job_country = request.POST.get('JOB_COUNTRY')
        job_location = request.POST.get('JOB_LOCATION')
        job_posted_date = request.POST.get('JOB_POSTED_DATE')
        job_application_end_date = request.POST.get('JOB_APPLICATION_END_DATE')
        job_nature = request.POST.get('JOB_NATURE')
        job_education_experience = request.POST.get('JOB_EDUCATION_EXPERIENCE')
        job_required_knowledge = request.POST.get('JOB_REQUIRED_KNOWLEDGE')
        job_number_of_vacancy = request.POST.get('JOB_NUMBER_OF_VACANCY')
        job_salary = request.POST.get('JOB_SALARY')
        
        # Update the job details in the database
        EMPLOYER_post_a_job.objects.filter(id=job_id).update(
            JOB_TITLE=job_title,
            JOB_POSITION=job_position,
            JOB_DESCRIPTION=job_description,
            JOB_STATE=job_state,
            JOB_COUNTRY=job_country,
            JOB_LOCATION=job_location,
            JOB_POSTED_DATE=job_posted_date,
            JOB_APPLICATION_END_DATE=job_application_end_date,
            JOB_NATURE=job_nature,
            JOB_EDUCATION_EXPERIENCE=job_education_experience,
            JOB_REQUIRED_KNOWLEDGE=job_required_knowledge,
            JOB_NUMBER_OF_VACANCY=job_number_of_vacancy,
            JOB_SALARY=job_salary
        )
      
        return redirect('index')

    context = {
            'job' : job
        }
        
    return render(request, 'editjobdetails.html',context)




# def edit_jobdetails(request):

#     return render(request, 'editjobdetails.html')
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4

def jobseeker_profile(request):
    EMAIL = request.session.get('EMAIL')
    jobseeker = User_jobseeker.objects.get(EMAIL=EMAIL)
    
    context = {
        'jobseeker': jobseeker
    }
    return render(request, 'jobseekerprofile.html', context)



def jobseeker_details(request):
    EMAIL = request.session.get('EMAIL')
    print(EMAIL)
    if request.method == 'POST':
        jobseeker_name = request.POST.get('jobseeker_name')
        jobseeker_profession = request.POST.get('jobseeker_profession')
        jobseeker_mobilenumber = request.POST.get('jobseeker_mobilenumber')
        jobseeker_address = request.POST.get('jobseeker_address')
        jobseeker_education = request.POST.get('jobseeker_education')
        jobseeker_skills = request.POST.get('jobseeker_skills')
        jobseeker_state = request.POST.get('jobseeker_state')
        jobseeker_location = request.POST.get('jobseeker_location')
        jobseeker_experience = request.POST.get('jobseeker_experience')
        jobseeker_englishlevel = request.POST.get('jobseeker_englishlevel')

        User_jobseeker.objects.filter(
            EMAIL=EMAIL).update(jobseeker_name=jobseeker_name,
                                jobseeker_profession=jobseeker_profession,
                                jobseeker_mobilenumber=jobseeker_mobilenumber,
                                jobseeker_address=jobseeker_address,
                                jobseeker_education=jobseeker_education,
                                jobseeker_skills=jobseeker_skills,
                                jobseeker_state=jobseeker_state,
                                jobseeker_location=jobseeker_location,
                                jobseeker_experience=jobseeker_experience,
                                jobseeker_englishlevel=jobseeker_englishlevel
                                )

        return redirect('jobseeker_profile')
    
    return redirect('index')
 
# def Edit_jobseeker_profile(request):
#     return render(request, 'editjobseekerprofile.html')


def Edit_jobseeker_profile(request):


    EMAIL = request.session.get('EMAIL')
    jobseeker = User_jobseeker.objects.get(EMAIL=EMAIL)
    
    context = {
        'jobseeker': jobseeker
    }

    return render(request, 'editjobseekerprofile.html',context)





def Edit_jobseeker_image_resume(request):
        EMAIL = request.session.get('EMAIL')
        if request.method == 'POST':
            jobseeker_IMAGE = request.FILES.get('jobseeker_IMAGE')
            jobseeker_resume = request.FILES.get('jobseeker_resume')

            data=User_jobseeker.objects.get(EMAIL=EMAIL)

            if jobseeker_IMAGE !=None:
                data.jobseeker_IMAGE=jobseeker_IMAGE

            if jobseeker_resume !=None:   
                data.jobseeker_resume=jobseeker_resume
            data.save()

            return redirect('jobseeker_profile')

        return redirect('index')



<<<<<<< HEAD
=======

>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
def apply_job(request,empye_id):


    EMAIL = request.session.get('EMAIL')
    jobseeker =  User_jobseeker.objects.get(EMAIL=EMAIL)
    job_post =EMPLOYER_post_a_job.objects.get (id=empye_id)
    
    new_application = jobseeker_apply_job(
<<<<<<< HEAD
        user=jobseeker,
        status=True,
        DETAILS_OF_EMPLOYER=jobseeker,
=======
        user=EMAIL,
        
        DETAILS_OF_EMPLOYEE=jobseeker,
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
        DETAILS_OF_JOB=job_post
    )
    new_application.save()

<<<<<<< HEAD
    return redirect('index')  


def employer_dashboard(request,job_id):
    EMAIL = request.session.get('EMAIL')
    applicants = jobseeker_apply_job.objects.filter(DETAILS_OF_JOB=job_id)
    
    context={
        'applicants':applicants
    }
    return render(request,'employerdashboard.html',context)

    
  

=======
    print(empye_id)

    return redirect('index')  


>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
def post_job_list(request):
    EMAIL = request.session.get('EMAIL')
    uid=User_employer.objects.get(EMAIL=EMAIL)

    jb= EMPLOYER_post_a_job.objects.filter(DETAILS_OF_COMPANY=uid.id)
    print(jb)
    context={
        'jb':jb
    }
 
    return render(request, 'listingAllJOb.html',context)


<<<<<<< HEAD
def job_accept(request,j_id):
    EMAIL = request.session.get('EMAIL')
    jobseeker_apply_job.objects.filter(id=j_id).update(status="True")
=======



def employer_dashboard(request,job_id):
    EMAIL = request.session.get('EMAIL')
    applicants = jobseeker_apply_job.objects.filter(DETAILS_OF_JOB=job_id,status=False,reject=False)
    
    context={
        'applicants':applicants
    }
    return render(request,'employerdashboard.html',context)


    
  



def job_accept(request,j_id):
    EMAIL = request.session.get('EMAIL')
    jobseeker_apply_job.objects.filter(id=j_id).update(status=True)
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4

    SUBJECT = 'Job Application Accepted'
    MESSAGE = f'Congratulations, your application  has been accepted!'
    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)

    return redirect('post_job_list')

<<<<<<< HEAD
def job_reject(request, r_id):
    EMAIL = request.session.get('EMAIL')
    jobseeker_apply_job.objects.filter(id=r_id).update(status=False)  # Use Boolean value False instead of string "False"
=======


def job_reject(request, r_id):
    EMAIL = request.session.get('EMAIL')
    jobseeker_apply_job.objects.filter(id=r_id).update(reject=True)  
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4

    SUBJECT = 'Job Application Rejected'
    MESSAGE = 'Dear , we regret to inform you that your application has been rejected.'  

    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)
<<<<<<< HEAD
=======
    print('EMAIL')
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4
    
    return redirect('post_job_list')



<<<<<<< HEAD



         
=======
# def accepted_applications(request):
#     EMAIL = request.session.get('EMAIL')
#     print(EMAIL)
    
#     # Directly fetch the applications with status=True for the logged-in user
#     ac = jobseeker_apply_job.objects.filter(user=EMAIL, status=True)
#     print(ac)
    
#     context = {
#         'ac': ac
#     }
    
#     return render(request, 'acceptedapplications.html', context)





def accepted_applications(request):
    EMAIL = request.session.get('EMAIL')
    
    uid = User_employer.objects.filter(EMAIL=EMAIL)  
    eid = 0
    for i in uid:
        eid = i.id
    
    print(EMAIL)
    print(eid)
    
    myjob = []
    
   
    dt = EMPLOYER_post_a_job.objects.filter(DETAILS_OF_COMPANY=eid)
    
    for j in dt:
        al = jobseeker_apply_job.objects.filter(DETAILS_OF_JOB=j.id, status=True)
        myjob.append(al)
        re = jobseeker_apply_job.objects.filter(DETAILS_OF_EMPLOYEE=eid, status=True)

    
    print(myjob, 'Accepted applications]]')
    
    context = {
        'ac': myjob
    }
    
    return render(request, 'acceptedapplications.html', context)





def rejected_applications(request):
    EMAIL = request.session.get('EMAIL')
    uid=User_employer.objects.filter(EMAIL=EMAIL)  
    eid=0
    for i in uid:
        eid=i.id
    print(EMAIL)
    print(eid)
    myjob=[]
    dt=EMPLOYER_post_a_job.objects.filter(DETAILS_OF_COMPANY=eid)
    for j in dt:
        al=jobseeker_apply_job.objects.filter(DETAILS_OF_JOB=j.id, reject=True)
        myjob.append(al)
    # Directly fetch the applications with reject=True for the logged-in user
    re = jobseeker_apply_job.objects.filter(DETAILS_OF_EMPLOYEE=eid, reject=True)
    print(myjob,']]')
    context = {
        're': myjob
    }
    
    return render(request, 'rejectedapplications.html', context)
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4











<<<<<<< HEAD
=======
def jobseeker_activity(request):

    EMAIL = request.session.get('EMAIL')

    ja_list = jobseeker_apply_job.objects.filter(user=EMAIL)
    
    context = {
        'ja_list': ja_list
    }
 
    return render(request, 'jobseekeractivity.html', context)



def jobseeker_successjobs(request):

    EMAIL = request.session.get('EMAIL')

    jsj_list = jobseeker_apply_job.objects.filter(user=EMAIL,status=True )
    
    context = {
        'jsj_list': jsj_list
    }
 
    return render(request, 'JobseekerSuccessJobs.html', context)


def jobseeker_failurejobs(request):


    EMAIL = request.session.get('EMAIL')

    jfj_list = jobseeker_apply_job.objects.filter(user=EMAIL,reject=True )
    
    context = {
        'jfj_list': jfj_list
    }
 
    return render(request, 'JobseekerFailureJobs.html', context)
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4




<<<<<<< HEAD
=======
def admin_dashboard(request):
    EMAIL = request.session.get('EMAIL')
    empf = User_employer.objects.all()
    context ={
        'empf' : empf
    }

    return render(request,'AdminDashboard.html',context)


def jobseeker_dashboard(request):
    EMAIL = request.session.get('EMAIL')
    jopf = User_jobseeker.objects.all()
    context ={
        'jopf' : jopf
    }

    return render(request,'jobseekerdashboard.html',context)


def alljobs_dashboard(request):
    EMAIL = request.session.get('EMAIL')
    alljob = EMPLOYER_post_a_job.objects.all()
    context ={
        'alljob' : alljob

    }

    return render(request,'AllJobsDashboard.html',context)
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4




<<<<<<< HEAD

    






=======
def video(request):
    return render(request,"video.html")
def analitycs(request):
    return render(request,"analitycs.html")

def sendmessage(request):
    return render(request,"sendmessage.html")

def search(request):
    return render(request,"search.html")
def news(request):
    return render(request,"news.html")



def employer_delete(request,data_id):
    EMAIL = request.session.get('EMAIL')
    User_employer.objects.filter(id=data_id).delete()

    SUBJECT = 'Your profile rejected'
    MESSAGE = f'your profile  has been rejected!'
    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)

    return redirect(admin_dashboard)


def jobseeker_delete(request,da_id):
    EMAIL = request.session.get('EMAIL')
    User_jobseeker.objects.filter(id=da_id).delete()
    SUBJECT = 'Your profile rejected'
    MESSAGE = f'your profile  has been rejected!'
    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)
    return redirect(jobseeker_dashboard)


def job_search(request):
    query_title = request.GET.get('job_title', '')
    # query_location = request.GET.get('location', '')
    print(query_title)

    # Filter the job posts based on the search criteria
    jobs = EMPLOYER_post_a_job.objects.filter(JOB_TITLE=query_title)
    print(jobs)
    context = {
        'jobs': jobs,
     
    }
    
    return render(request, 'search.html', context)



def changepassword(request):
    return render(request,"changepassword.html")



def jobseekerProfilePasswordUpdate(request):
    EMAIL = request.session.get('EMAIL')

    # Fetch the jobseeker using the email stored in session
  
    jobseekerDetails = User_jobseeker.objects.get(EMAIL=EMAIL)
  
    if not EMAIL:
        return redirect('jobseeker_profile')

    if request.method == 'POST':
        current_password = request.POST.get("password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")


        # Check if the entered current password matches the stored (hashed) password
        if jobseekerDetails:
            if new_password == confirm_password:
                # Hash the new password before saving
                jobseekerDetails.PASSWORD =new_password
                jobseekerDetails.save()
                print("PASSWORD UPDATED")
                return redirect('jobseeker_profile')
            else:
                print("New passwords do not match.")
        else:
            print("Current password is incorrect.")

    return render(request, "jobseekerprofile.html", {'jobseekerDetails': jobseekerDetails})


def dashdel_job(request,data_id):
    job = EMPLOYER_post_a_job.objects.filter(id=data_id)
    if job.exists():
        job.delete()
    return redirect('alljobs_dashboard')



def admin_employerProfile(request,empr_id):
    
    employer =  User_employer.objects.get(id=empr_id)
    context ={
        'employer' : employer

        
    }
    

    return render(request,"AdminEmployerProfile.html",context)


def Admin_Employeraccept(request,j_id):
    EMAIL = request.session.get('EMAIL')
    User_employer.objects.filter(id=j_id).update(verify=True)
    print(j_id)
    SUBJECT = 'Your profile Accepted'
    MESSAGE = f'Congratulations, your profile  has been accepted!'
    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)

    return redirect('admin_dashboard')


    

def admin_jobseekerProfile(request,empe_id):
    
    jobseeker =  User_jobseeker.objects.get(id=empe_id)
    context ={
        'jobseeker' : jobseeker

        
    }
    

    return render(request,"AdminJobseekerProfile.html",context)

def Admin_jobseekeraccept(request,j_id):
    EMAIL = request.session.get('EMAIL')
    User_jobseeker.objects.filter(id=j_id).update(verify=True)
    print(j_id)
    SUBJECT = 'Your profile Accepted'
    MESSAGE = f'Congratulations, your profile  has been accepted!'
    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)

    return redirect('admin_dashboard')


def admin_AlljobsDetails(request,jo_id):
    
    job =  EMPLOYER_post_a_job.objects.get(id=jo_id)
    context ={
        'job' : job

        
    }
    

    return render(request,"AdminAllJobs.html",context)
>>>>>>> 0133ccfa30fe07cdb7d6867cc3c5465c95f493f4




            




































         



