import random
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages








def index(request):
    try:
        EMAIL=request.session['EMAIL']
        emp=User_employer.objects.get(EMAIL=EMAIL)
        
        data = EMPLOYER_post_a_job.objects.filter(DETAILS_OF_COMPANY=emp)


        context = {
            'data': data,


        
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





def job_details(request,job_id):

    
    job = EMPLOYER_post_a_job.objects.get(id=job_id)
   

    context = {
        'job': job

       
    }
    return render(request, 'job_details.html',context)



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
        else:
            messages.error(request,"Invalid email or password .Please Sign up")
            return redirect('signup')
        
        
        
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



def apply_job(request,empye_id):


    EMAIL = request.session.get('EMAIL')
    jobseeker =  User_jobseeker.objects.get(EMAIL=EMAIL)
    job_post =EMPLOYER_post_a_job.objects.get (id=empye_id)
    
    new_application = jobseeker_apply_job(
        user=jobseeker,
        status=True,
        DETAILS_OF_EMPLOYER=jobseeker,
        DETAILS_OF_JOB=job_post
    )
    new_application.save()

    return redirect('index')  


def employer_dashboard(request,job_id):
    EMAIL = request.session.get('EMAIL')
    applicants = jobseeker_apply_job.objects.filter(DETAILS_OF_JOB=job_id)
    
    context={
        'applicants':applicants
    }
    return render(request,'employerdashboard.html',context)

    
  

def post_job_list(request):
    EMAIL = request.session.get('EMAIL')
    uid=User_employer.objects.get(EMAIL=EMAIL)

    jb= EMPLOYER_post_a_job.objects.filter(DETAILS_OF_COMPANY=uid.id)
    print(jb)
    context={
        'jb':jb
    }
 
    return render(request, 'listingAllJOb.html',context)


def job_accept(request,j_id):
    EMAIL = request.session.get('EMAIL')
    jobseeker_apply_job.objects.filter(id=j_id).update(status="True")

    SUBJECT = 'Job Application Accepted'
    MESSAGE = f'Congratulations, your application  has been accepted!'
    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)

    return redirect('post_job_list')

def job_reject(request, r_id):
    EMAIL = request.session.get('EMAIL')
    jobseeker_apply_job.objects.filter(id=r_id).update(status=False)  # Use Boolean value False instead of string "False"

    SUBJECT = 'Job Application Rejected'
    MESSAGE = 'Dear , we regret to inform you that your application has been rejected.'  

    send_mail(SUBJECT, MESSAGE, settings.EMAIL_HOST_USER, [EMAIL], fail_silently=False)
    
    return redirect('post_job_list')






         




















    










            




































         



