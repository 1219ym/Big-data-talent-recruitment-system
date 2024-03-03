
from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    job_category = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    education_level = models.CharField(max_length=200)
    experience_time = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    shift = models.CharField(max_length=200)
    job_description = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.job_title
    

# Create your models here.
