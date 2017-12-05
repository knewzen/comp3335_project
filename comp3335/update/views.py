from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
#from django.conf import setting
from comp3335.course.models import Course
from comp3335.message.models import Message
from comp3335.utils.encryption import *
from comp3335.account.models import Account
import re
# Create your views here.
@csrf_exempt
def checkPassword(pwd):
    if len(pwd) < 8:
        return False
    digit_flag = False
    lower_flag = False
    upper_flag = False
    for i in pwd:
        if i.isdigit():
            digit_flag = True
        if i.islower():
            lower_flag = True
        if i.isupper():
            upper_flag = True
    return digit_flag and lower_flag and upper_flag

@csrf_exempt
def update(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        email = request.session['authorized']

        if request.POST["age"].isdigit():
            a = int(request.POST["age"])
            if not ( a > 0 and a < 150 ):
                return render(request, 'update/index.html', {"err": "Please enter a valid age."})
        else:
            return render(request, 'update/index.html', {"err": "Please enter a valid age."})
       

        pwd1 = request.POST["password"]
        pwd2 = request.POST["password2"]

        if pwd1 != pwd2:
            #####
            #####    add error message handling
            #####   password not matching
            return render(request, 'update/index.html', {"err": "The passwords must match."})
        
        if not checkPassword(pwd1):
            #pass
            return render(request, 'update/index.html', {"err": "The password must have at least one lower case letter, one upper case letter and one digit."})
        

        
        
        salt1 = generate_salt()
        salt2 = generate_salt()
        salt = encrypt(salt2, pwd1)

        f_name = encrypt(request.POST["f_name"], salt)
        l_name = encrypt(request.POST["l_name"], salt)
        age = encrypt(request.POST["age"], salt)
        pwd_hash = hash_func(pwd1, salt1)

        if len(f_name) > 90 or len(l_name) > 90 or len(salt1) > 255 or len(salt2) > 255 or len(age) > 64:
            return render(request, 'account/register.html', {"err": "Sorry... Some fields are too long."})
        Account.objects.filter(email=email).update(f_name=f_name, l_name=l_name, age=age, pwd_hash=pwd_hash, salt1=salt1, salt2=salt2)
        
        
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'update/index.html', {})

    return redirect('/dashboard/')

# Create your views here.

