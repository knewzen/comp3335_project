from django.shortcuts import render, redirect
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
	try:
		authorized = request.session['authorized']
	except KeyError:
		return redirect('/account/register.html')
	course1 = request.POST["search"]

	courseResult = Course.objects.all()
	msgResult = Message.objects.all()

	c = []
	m = []

	for course in courseResult:
		course.name = msg_decrypt(course.name)
		course.code = msg_decrypt(course.code)
		if course1.lower() in course.name.lower() or course1.lower() in course.code.lower():
			c.append({"name": course.name, "code":course.code, "id":course.id})

	for msg in msgResult:
		msg.text = msg_decrypt(msg.text)
		if course1.lower() in msg.text.lower():
			m.append({"id" : msg.id, "text":msg.text, "user_id":msg.user_id, "course_id":msg.course_id})

	context = {"course":c,"msg":m}
	#print(context)
	return render(request,'search/SearchResult.html',context)