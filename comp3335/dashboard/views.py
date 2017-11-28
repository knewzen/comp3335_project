

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from comp3335.course.models import Course
from comp3335.message.models import Message
from comp3335.utils.encryption import *

import logging

logging.basicConfig(filename='log/test.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


def index(request):
    # get courses from database
    test_courses= Course.objects.all()
    for c in test_courses:
        c.name = msg_decrypt(c.name)
        c.code = msg_decrypt(c.code)
    for c in test_courses:
        print(c.name)
        print(c.code)
        
    logging.info('request course list for dashboard')

    return render(request, 'dashboard/board/index.html', {'courses': test_courses})

def coursedetail(request, course_id):


    courseResult = Course.objects.all()
    msgResult = Message.objects.all()

    c = []
    m = []
    find = False

    for course in courseResult:
        course.code = msg_decrypt(course.code)
        course.name = msg_decrypt(course.name)
        if course_id in course.code:
            c={"name":course.name,"code":course.code}
            find = True

    for msg in msgResult:
        msg.text = msg_decrypt(msg.text)
        if course_id in msg.course_id:
            m.append({"id" : msg.id, "text":msg.text, "user_id":msg.user_id, "course_id":msg.course_id})

    if find:
        logging.info("request course detail success: course code = " + course_id)
    else:
        logging.warn("request course detail failed: course code = " + str(course_id))
        return HttpResponseRedirect('/dashboard')
    print(c)
    return render(request, 'dashboard/board/coursedetail.html', {'course': c, 'messages':m})

def getmessage(request):
    course_id = request.POST['course_id']
    course_code = request.POST['course_code']
    message = request.POST['message']


    #get id of course where code = course_id
    # course = Course.objects.filter(code=course_id)


    # insert into database
    # if message:
    #     test_insert = Message.objects.create(text=message, course_id=course[0].id, user_id=1)
    #     logging.info("insert message: course code = " + course_id + ", message = " +message)
    #     test_insert.save()

    # messages = Message.objects.filter(code=course[0].id)

    messages = ['a','test']
    logging.info("insert message: course code = " + course_code + ", message = " + message)

    return JsonResponse(messages, safe=False)

