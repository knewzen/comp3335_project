from django.shortcuts import render
from comp3335.util.hash import *
# Create your views here.
def register(request):
	hashed_password = hash_func(password, salt)