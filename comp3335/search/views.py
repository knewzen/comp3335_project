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
	course = msg_encrypt(request.POST["course"])
	msg = msg_encrypt(request.POST["msg"])
	

	print(course, msg)
	#course_encrypted = course_encrypt(course)
	#courseResult = Course.objects.all()
	# id code name
	# id text course_id user_id
	#filer(name=)
	courseResult = Course.objects.all()
	msgResult = Message.objects.all()

	for course in courseResult:
		course.name = msg_decrypt(course.name)
		course.code = msg_decrypt(code)

	for msg in msgResult:
		msg.text = msg_decrypt(msg.text)

	courseResult = courseResult.objects.filter(Q(name__icontains=course)|Q(code__icontains=course))
	msgResult = msgResult.objects.filter(text__icontains=msg)

	#courseResult = Course.objects.filter(Q(name__icontains=course)|Q(code__icontains=course))
	#msgResult = Message.objects.filter(text__icontains=msg)


	#User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))
	print(dir(courseResult))
	#context = {"Course":[{"name" : "comp2323"},{"name":"comp2222"}]}
	#context = {"course":msg_decrypt(courseResult),"msg":msg_decrypt(msgResult)}
	context = {"course":(courseResult),"msg":(msgResult)}

	return render(request,'search/SearchResult.html',context)
	