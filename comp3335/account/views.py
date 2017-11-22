from django.shortcuts import render
from comp3335.utils.encryption import *
from .forms import RegisterForm
from django.http import HttpResponseRedirect
# Create your views here.

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


def auth(request):
    print(request.POST["email"])
    print(request.POST["password"])    

    return HttpResponseRedirect('/account/') 