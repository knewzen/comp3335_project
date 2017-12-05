from django.contrib import admin
from .models import Account

from comp3335.utils.encryption import *
from simple_history.admin import SimpleHistoryAdmin
# Create your models here.


class AccountAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # custom stuff here
        if not re.match('[a-zA-Z]+[0-9]+', obj.code):
        	print("here")
        	return

        obj.f_name = msg_encrypt(obj.f_name)
        obj.l_name = msg_encrypt(obj.l_name)
        obj.age = msg_encrypt(obj.age)

        if len(obj.f_name) > 100 or len(obj.l_name) > 100:
        	return
        obj.save()

admin.site.register(Account, SimpleHistoryAdmin)

# Register your models here.
