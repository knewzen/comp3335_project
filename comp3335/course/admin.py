from django.contrib import admin
import re
from .models import Course
from comp3335.utils.encryption import *
# Create your models here.


class CourseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # custom stuff here
        if not re.match('[a-zA-Z]+[0-9]+', obj.code):
        	print("here")
        	return
        print(obj.code)
        print(re.match('[a-zA-Z]+[0-9]+', obj.code))
        obj.code = msg_encrypt(obj.code)
        obj.name = msg_encrypt(obj.name)

        if len(obj.code) > 100 or len(obj.name) > 100:
        	return
        obj.save()

admin.site.register(Course, CourseAdmin)