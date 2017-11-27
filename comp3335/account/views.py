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

        pwd1 = request.POST["password"]
        pwd2 = request.POST["password2"]
        if pwd1 != pwd2:
            render(request, 'account/register.html')
        # create a form instance and populate it with data from the request:
        email = msg_encrypt(request.POST["email"])

        if Account.objects.filter(email=email).exists():
            return render(request, 'account/register.html', {})

        f_name = msg_encrypt(request.POST["f_name"])
        l_name = msg_encrypt(request.POST["l_name"])
        age = msg_encrypt(request.POST["age"])

        salt = generate_salt()

        pwd_hash = hash_func(pwd1, salt)
        acct = Account(email=email, f_name = f_name, l_name = l_name, age=age, pwd_hash = pwd_hash, salt = salt)
        acct.save()
        return render(request, 'account/index.html', {})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        return render(request, 'account/register.html', {"form" : form})
    
@csrf_exempt

def auth(request):

    username = msg_encrypt(request.POST["email"])
    pwd = request.POST["password"]    

    print("*"*100)
    if not Account.objects.filter(email=username).exists():
        print("fail")
        return render(request, 'account/index.html', {}) 
    print("*"*100)
    iden = Account.objects.get(email=username)
    
    if hash_func(pwd, iden.salt) == iden.pwd_hash:
        print("success")
        return render(request, 'account/index.html', {})
    else:
        print("fail")
        return render(request, 'account/index.html', {}) 
    
        