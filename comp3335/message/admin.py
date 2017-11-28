from django.contrib import admin
from .models import Message

from comp3335.utils.encryption import *
# Create your models here.


class MessageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # custom stuff here
        obj.text = msg_encrypt(obj.text)
        
        if len(text) > 10000:
        	return
        obj.save()

admin.site.register(Message, MessageAdmin)
# Register your models here.
