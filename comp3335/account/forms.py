from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    f_name = forms.CharField(label="First Name", max_length=30)
    l_name = forms.CharField(label="Last Name", max_length=30)
    age = forms.IntegerField(label="Age")
    pwd = forms.CharField(label="Password",max_length=255,widget=forms.PasswordInput)
    pwd2 = forms.CharField(label="Re-type password", max_length=255,widget=forms.PasswordInput)



    def is_valid(self):
    	valid = super(RegisterForm, self).is_valid()

    	if valid and self.pwd == self.pwd2:
    		return True
    	else:
    		return False