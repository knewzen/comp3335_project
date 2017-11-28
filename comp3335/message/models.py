from django.db import models
from comp3335.account.models import Account
from comp3335.course.models import Course

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=10000, null=False)
    timestamp = models.CharField(max_length=120, null=False)
    user = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)