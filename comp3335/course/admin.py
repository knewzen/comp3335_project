from django.contrib import admin

from .models import Course
from comp3335.utils.encryption import *
# Create your models here.


class CourseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # custom stuff here
        print(change)
        print(obj.code, obj.name)
        obj.code = msg_encrypt(obj.code)
        obj.name = msg_encrypt(obj.name)
        print(obj.code, obj.name)
        obj.save()

admin.site.register(Course, CourseAdmin)