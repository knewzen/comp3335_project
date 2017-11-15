from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=100, unique=True, null=False)
    pwd_hash = models.CharField(max_length=255, null=False)
    salt = models.CharField(max_length=255, null=False)
    f_name = models.CharField(max_length=30, null=False)
    l_name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)