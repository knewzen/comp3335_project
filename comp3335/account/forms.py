from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField()
    pwd = forms.CharField(max_length=255)
    f_name = forms.CharField(max_length=30)
    l_name = forms.CharField(max_length=30)
    age = forms.IntegerField()