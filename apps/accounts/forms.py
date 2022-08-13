from django import  forms
from  django.contrib.auth.forms import UserCreationForm
from accounts.models import User



class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')