from django.db import models
from comp3335.utils.encryption import *
from simple_history.models import HistoricalRecords

# Create your models here.



class Course(models.Model):
    code = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return msg_decrypt(self.code) + " "+ msg_decrypt(self.name)
        #return (self.code) + " "+ (self.name)