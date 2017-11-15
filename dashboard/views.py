from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    test_courses = ['COMP3335', 'COMP3421']
    return render(request, 'dashboard/board/index.html', {'courses': test_courses})

def coursedetail(request, course_id):
    return render(request, 'dashboard/board/coursedetail.html', {'course_id': course_id})