

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    # get courses from database
    test_courses = ['COMP3335', 'COMP3421']
    return render(request, 'dashboard/board/index.html', {'courses': test_courses})

def coursedetail(request, course_id):
    return render(request, 'dashboard/board/coursedetail.html', {'course_id': course_id})

def getmessage(request):
    course_id = request.POST['course_id']
    message = request.POST['message']

    messages = ['a', 'hi']

    # insert into database
    if message:
        messages.append(message)

    return JsonResponse(messages, safe=False)