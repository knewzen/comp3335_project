

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from comp3335.course.models import Course
from comp3335.message.models import Message

def index(request):
    # get courses from database
    # test_courses = ['COMP3335', 'COMP3421']
    test_courses= Course.objects.all()
    return render(request, 'dashboard/board/index.html', {'courses': test_courses})

def coursedetail(request, course_id):
    course = Course.objects.filter(code='COMP3335')
    messages = Message.objects.filter(course_id=course[0].id)

    return render(request, 'dashboard/board/coursedetail.html', {'course': course[0], 'messages':messages})

def getmessage(request):
    course_id = request.POST['course_id']
    message = request.POST['message']


    #get id of course where code = course_id
    course = Course.objects.filter(code=course_id)

    # insert into database
    if message:
        test_insert = Message.objects.create(text=message, course_id=course[0].id, user_id=1)
        test_insert.save()

    messages = Message.objects.filter(code=course[0].id)

    return JsonResponse(messages, safe=False)