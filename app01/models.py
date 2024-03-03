import email
from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    username = models.CharField(max_length=32, verbose_name='用户名')
    email    = models.CharField(max_length=32, verbose_name='邮箱')
    password = models.CharField(verbose_name='密码', max_length=64)
# Create your models here.
