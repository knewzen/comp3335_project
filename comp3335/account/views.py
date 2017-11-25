from django.shortcuts import render
from comp3335.utils.encryption import *
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from comp3335.account.models import Account
# Create your views here.

@csrf_exempt
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/account/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, '/account/', {'form': form})

@csrf_exempt
def auth(request):

    username = request.POST["email"]
    pwd = request.POST["password"]    


    iden = Account.objects.filter(email=username)

    context = {"uesrname":iden}

    match = False

    if match:
        return render(request, 'account/success.html', context)
    else:
        return render(request, 'account/index.html', context) 