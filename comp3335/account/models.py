from django.db import models

#from djangoaudit.models import AuditedModel

# Create your models here.
class Account(models.Model):
<<<<<<< HEAD
    log_fields = ('email','pwd_hash','salt','f_name','l_name','age')

    email = models.EmailField(unique=True, null=False)
    pwd_hash = models.CharField(max_length=255, null=False)
    salt = models.CharField(max_length=255, null=False)
    f_name = models.CharField(max_length=30, null=False)
    l_name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)

    def __unicode__(self):
        return self.email
=======
    email = models.EmailField(unique=True,null=False) #noEncrypt
    pwd_hash = models.CharField(max_length=255, null=False) #noEncrypt
    salt = models.CharField(max_length=255, null=False) #noEncrypt
    f_name = models.CharField(max_length=90, null=False)
    l_name = models.CharField(max_length=90, null=False)
    age = models.CharField(max_length=64,null=False)
>>>>>>> ed7ea8158678fd81d1112ce91f9066120fa28863
