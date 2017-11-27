from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(unique=True, null=False) #noEncrypt
    pwd_hash = models.CharField(max_length=255, null=False) #noEncrypt
    salt = models.CharField(max_length=255, null=False) #noEncrypt
    f_name = models.CharField(max_length=90, null=False)
    l_name = models.CharField(max_length=90, null=False)
    age = models.CharField(max_length=64,null=False)