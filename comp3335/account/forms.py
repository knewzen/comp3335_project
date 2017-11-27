from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    f_name = forms.CharField(label="First Name", max_length=30)
    l_name = forms.CharField(label="Last Name", max_length=30)
    age = forms.IntegerField(label="Age")
    pwd = forms.CharField(label="Password",max_length=255)
    pwd2 = forms.CharField(label="Re-type password", max_length=255)