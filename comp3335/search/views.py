from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def search(request):
	course = request.POST["course"]
	msg = request.POST["msg"]
	
	context = {"Course":[{"name" : "comp2323"},{"name":"comp2222"}]}

	print(course,msg)

	return render(request,'SearchResult.html',context)
	