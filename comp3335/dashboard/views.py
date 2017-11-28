

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from comp3335.course.models import Course
from comp3335.message.models import Message
from comp3335.account.models import Account
from comp3335.utils.encryption import *

import logging

logging.basicConfig(filename='log/test.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


def index(request):
    # get courses from database
    test_courses= Course.objects.all()
    for c in test_courses:
        c.name = msg_decrypt(c.name)
        c.code = msg_decrypt(c.code)
    logging.info('request course list for dashboard')

    return render(request, 'dashboard/board/index.html', {'courses': test_courses})

def coursedetail(request, course_id):


    courseResult = Course.objects.all()
    msgResult = Message.objects.all()

    c = []
    m = []
    find = False

    #the course_id is lile "COMP1111" ! no the id of the course object
    for course in courseResult:
        course.code = msg_decrypt(course.code)
        course.name = msg_decrypt(course.name)
        if course_id in course.code:
            c={"name":course.name,"code":course.code}
            find = True

    for msg in msgResult:
        msg.text = msg_decrypt(msg.text)
        if course.id == msg.course_id:
            m.append({"id" : msg.id, "text":msg.text, "user_id":msg.user_id, "course_id":msg.course_id})

    if find:
        logging.info("request course detail success: course code = " + course_id)
    else:
        logging.warn("request course detail failed: course code = " + str(course_id))
        return HttpResponseRedirect('/dashboard')
    print(m)
    return render(request, 'dashboard/board/coursedetail.html', {'course': c, 'messages':m})

def getmessage(request):
    course_code = request.POST['course_code']
    message = request.POST['message']

    courseResult = Course.objects.all()

    m = []
    m.append(message)
    #get id of course where code = course_id
    # course = Course.objects.filter(code=course_id)


    #hvn't finished!!!!
    if(len(msg_encrypt(message))>10000):
        return HttpResponseRedirect("too many")

    #course = Course.objects.first()
    user = Account.objects.first()
    for c in courseResult:
        enc_code = c.code
        c.code = msg_decrypt(c.code)
        if course_code in c.code:
            course = Course.objects.get(code = enc_code)
    msg = Message.objects.create(text=msg_encrypt(message),user=user,course=course)
    msg.save()
    logging.info("insert message: course code = " + course_code + ", message = " + message)


    return JsonResponse(m, safe=False)

