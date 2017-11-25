from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
#from django.conf import setting
from comp3335.course.models import Course
from comp3335.message.models import Message
from comp3335.utils.encryption import *
from comp3335.account.models import Account

# Create your views here.
@csrf_exempt
def search(request):
	course1 = request.POST["course"]
	msg1 = request.POST["msg"]
	courseResult = Course.objects.all()
	msgResult = Message.objects.all()

	c = []
	m = []

	for course in courseResult:
		#print("look----->",course.name)
		course.name = msg_decrypt(course.name)
		if course1 in course.name or course1 in course.code:
			c.append({"name": course.name, "code":course.code})

	for msg in msgResult:
		msg.text = msg_decrypt(msg.text)
		if msg1 in msg.text:
			m.append({"id" : msg.id, "text":msg.text, "user_id":msg.user_id, "course_id":msg.course_id})

	context = {"course":c,"msg":m}
	return render(request,'search/SearchResult.html',context)
