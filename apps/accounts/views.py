from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
from django.db import transaction
from .forms import RegisterForm
from .mixins import AuthMixin,SetSpecialMixin
from file.models import User
# Create your views here.
# login view
class Login(AuthMixin,LoginView):
    template_name = "account/login.html"
    @transaction.atomic
    def get_success_url(self):
        messages.success(self.request, 'You were logged in successfully')
        return reverse_lazy('file:home')


# Logout view
def Logout(request):
	logout(request) if request.user.is_authenticated else redirect("account:register")
	return redirect("account:register")

# Set special page
class SetSpecial(SetSpecialMixin,TemplateView):
    template_name = "account/SetSpecial.html"
    def post(self,request):
        User.objects.filter(username=self.request.user.username).update(
            is_special = True,
            limit=50
        )
        messages.success(self.request, 'from now on, you are a special user')
        return redirect("file:home")

#404 page
def handler404(request,exception):
    return render(request,"404/404.html")
