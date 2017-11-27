from django.shortcuts import render
from comp3335.utils.encryption import *
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from comp3335.account.models import Account
from comp3335.dashboard.views import *
from django.shortcuts import redirect
# Create your views here.

@csrf_exempt
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        pwd1 = request.POST["password"]
        pwd2 = request.POST["password2"]
        if pwd1 != pwd2:
            #####
            #####    add error message handling
            #####   password not matching
            return render(request, 'account/register.html')
        
        accts = Account.objects.all()

        for acct in accts:
            eemail = msg_decrypt(acct.email)
            if request.POST["email"] == eemail:
                #####
                #####    add error message handling
                #####   email already used
                return render(request, 'account/register.html')

        salt1 = generate_salt()
        salt2 = generate_salt()
        salt = encrypt(salt2, pwd1)

        email = msg_encrypt(request.POST["email"])
        f_name = encrypt(request.POST["f_name"], salt)
        l_name = encrypt(request.POST["l_name"], salt)
        age = encrypt(request.POST["age"], salt)
        pwd_hash = hash_func(pwd1, salt1)

        
        acct = Account(email=email, f_name = f_name, l_name = l_name, age=age, pwd_hash = pwd_hash, salt1 = salt1, salt2 = salt2)
        acct.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'account/register.html', {})

    return render(request, 'account/index.html', {})
@csrf_exempt

def auth(request):

    username = request.POST["email"]
    pwd = request.POST["password"]    

    accts = Account.objects.all()

    for acct in accts:
        eemail = msg_decrypt(acct.email)
        if eemail == username:
            if hash_func(pwd, acct.salt1) == acct.pwd_hash:
                print("Success")
                return redirect('/dashboard')
    
    
    print("fail")
    return render(request, 'account/index.html', {}) 
    
        