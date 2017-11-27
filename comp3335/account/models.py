from django.db import models

#from djangoaudit.models import AuditedModel

# Create your models here.
class Account(models.Model):
    log_fields = ('email','pwd_hash','salt','f_name','l_name','age')

    email = models.EmailField(unique=True, null=False)
    pwd_hash = models.CharField(max_length=255, null=False)
    salt = models.CharField(max_length=255, null=False)
    f_name = models.CharField(max_length=30, null=False)
    l_name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)

    def __unicode__(self):
        return self.email