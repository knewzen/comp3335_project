from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    email = models.EmailField(unique=True, null=False) #noEncrypt
    pwd_hash = models.CharField(max_length=255, null=False) #noEncrypt
    salt1 = models.CharField(max_length=255, null=False) #noEncrypt
    salt2 = models.CharField(max_length=255, null=False) #noEncrypt
    f_name = models.CharField(max_length=90, null=False)
    l_name = models.CharField(max_length=90, null=False)
    age = models.CharField(max_length=64,null=False)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()