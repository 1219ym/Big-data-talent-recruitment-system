from django.db import models

class Resume(models.Model):
    # 基本信息
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    address = models.TextField()

    # 教育经历
    education_info = models.TextField()
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50)
    major_name = models.CharField(max_length=100)
    extra_info1 = models.TextField(blank=True)

    # 工作经历
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    extra_info2 = models.TextField(blank=True)

    # 技能
    skill_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20)
