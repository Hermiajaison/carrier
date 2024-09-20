from django.db import models

# Create your models here.


class User_employer(models.Model):
    USERNAME=models.CharField(max_length=100)
    PASSWORD=models.CharField(max_length=100)
    EMAIL=models.EmailField(max_length=100)
    EMPLOYER_NAME=models.CharField(max_length=100)
    COMPANY_NAME=models.CharField(max_length=100)
    EMPLOYER_LOCATION=models.CharField(max_length=100)
    EMPLOYER_STATE=models.CharField(max_length=100)
    EMPLOYER_PROFESSION=models.CharField(max_length=100)
    EMPLOYER_AGE=models.CharField(max_length=100)
    EMPLOYER_JOB_NATURE=models.CharField(max_length=100)
    EMPLOYER_PHONE=models.CharField(max_length=100)
    EMPLOYER_IMAGE=models.ImageField(upload_to='profile_pfp',blank=True, null=True)
    COMPANY_LOGO=models.ImageField(upload_to='profile_pfp',blank=True, null=True)


class User_jobseeker(models.Model):
    USERNAME=models.CharField(max_length=100)
    PASSWORD=models.CharField(max_length=100)
    EMAIL=models.EmailField(max_length=100)
    jobseeker_name=models.CharField(max_length=100)
    jobseeker_profession=models.CharField(max_length=100)
    jobseeker_mobilenumber=models.CharField(max_length=100)
    jobseeker_address=models.CharField(max_length=100)
    jobseeker_education=models.CharField(max_length=100)
    jobseeker_skills=models.CharField(max_length=100)
    jobseeker_state=models.CharField(max_length=100)
    jobseeker_location=models.CharField(max_length=100)
    jobseeker_experience=models.CharField(max_length=100)
    jobseeker_englishlevel=models.CharField(max_length=100)
    jobseeker_IMAGE=models.ImageField(upload_to='profile_pfp',blank=True, null=True)
    jobseeker_resume=models.FileField(upload_to='profile_pfp',blank=True, null=True)





def __str__(self):
        return self.EMPLOYER_NAME

class EMPLOYER_post_a_job(models.Model):
    
    JOB_TITLE=models.CharField(max_length=100)
    JOB_POSITION=models.CharField(max_length=100)
    JOB_DESCRIPTION=models.CharField(max_length=700)
    JOB_STATE=models.CharField(max_length=100)
    JOB_COUNTRY=models.CharField(max_length=100)
    JOB_LOCATION=models.CharField(max_length=100)
    JOB_POSTED_DATE=models.CharField(max_length=100)
    JOB_APPLICATION_END_DATE=models.CharField(max_length=100)
    JOB_NATURE=models.CharField(max_length=100)
    JOB_EDUCATION_EXPERIENCE=models.CharField(max_length=200)
    JOB_REQUIRED_KNOWLEDGE=models.CharField(max_length=500)
    JOB_NUMBER_OF_VACANCY=models.CharField(max_length=100)
    JOB_SALARY=models.CharField(max_length=100)
    DETAILS_OF_COMPANY=models.ForeignKey(User_employer,on_delete=models.CASCADE)
    

class jobseeker_apply_job(models.Model):
    user=models.CharField(max_length=100)
    status=models.BooleanField()
    DETAILS_OF_EMPLOYER=models.ForeignKey(User_jobseeker,on_delete=models.CASCADE)
    DETAILS_OF_JOB=models.ForeignKey(EMPLOYER_post_a_job,on_delete=models.CASCADE)














     


    


    


    





