from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=30, unique=True, null=False)
    name = models.CharField(max_length=100, null=False)