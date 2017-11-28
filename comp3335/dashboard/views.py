
 
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from comp3335.course.models import Course
from comp3335.message.models import Message
from comp3335.account.models import Account
from comp3335.utils.encryption import *
from time import gmtime, strftime

import logging

logging.basicConfig(filename='log/test.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


def index(request):
    # get courses from database
    try:
        authorized = request.session['authorized']
    except KeyError:
        return redirect('/account/register.html')
    
    test_courses= Course.objects.all()
    for c in test_courses:
        c.name = msg_decrypt(c.name)
        c.code = msg_decrypt(c.code)
    logging.info('request course list for dashboard')
    print(request.session["authorized"])
    return render(request, 'dashboard/board/index.html', {'courses': test_courses})

def coursedetail(request, course_id):
    try:
        authorized = request.session['authorized']
    except KeyError:
        return redirect('/account/register.html')

    courseResult = Course.objects.all()
    msgResult = Message.objects.all()

    c = {}
    m = []
    find = False

    #the course_id is lile "COMP1111" ! no the id of the course object
    for course in courseResult:
        course.code = msg_decrypt(course.code)
        course.name = msg_decrypt(course.name)
        if course_id in course.code:
            c={"name":course.name,"code":course.code}
            find = True
            break

    if find:
        logging.info("request course detail success: course code = " + course_id)
    else:
        logging.warn("request course detail failed: course code = " + str(course_id))
        return HttpResponseRedirect('/dashboard')

    for msg in msgResult:
        msg.text = msg_decrypt(msg.text)
        if course.id == msg.course_id:

            m.append({"id" : msg.id, "text":msg.text, "user_id":msg.user_id, "course_id":msg.course_id,"time":msg_decrypt(msg.timestamp)})

    return render(request, 'dashboard/board/coursedetail.html', {'course': c, 'messages':m})

def getmessage(request):
    try:
        authorized = request.session['authorized']
    except KeyError:
        return redirect('/account/register.html')

    course_code = request.POST['course_code']
    message = request.POST['message']

    courseResult = Course.objects.all()

    m = []
    #m.append(message)
    #get id of course where code = course_id
    # course = Course.objects.filter(code=course_id)


    #hvn't finished!!!!
    if(len(msg_encrypt(message))>10000):
        return HttpResponseRedirect("too many")

    #course = Course.objects.first()
    

    user = Account.objects.get(email = authorized)
    
    for c in courseResult:
        enc_code = c.code
        c.code = msg_decrypt(c.code)
        if course_code in c.code:
            course = Course.objects.get(code = enc_code)
    time = msg_encrypt(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    msg = Message.objects.create(text=msg_encrypt(message),user=user,course=course,timestamp=time)
    msg.save()
    logging.info("insert message: course code = " + course_code + ", message = " + message)

    
    msgResult = Message.objects.all()
    for ms in msgResult:
        m.append("User ["+ msg_decrypt(ms.timestamp) + "]: "+msg_decrypt(ms.text))

    return JsonResponse(m, safe=False)
    #return redirect('/dashboard/board/coursedetail.html')
