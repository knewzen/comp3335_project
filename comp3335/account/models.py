from django.db import models
import audit
from django.contrib.auth.models import User
from comp3335.utils.encryption import *

# Create your models here.
class Account(models.Model):
    email = models.CharField(unique=True,max_length=255,null=False) #noEncrypt
    pwd_hash = models.CharField(max_length=255, null=False) #noEncrypt
    salt1 = models.CharField(max_length=255, null=False) #noEncrypt
    salt2 = models.CharField(max_length=255, null=False)
    f_name = models.CharField(max_length=90, null=False)
    l_name = models.CharField(max_length=90, null=False)
    age = models.CharField(max_length=64,null=False)


    history = audit.AuditTrail()

    def __str__(self):
        return msg_decrypt(self.email)
