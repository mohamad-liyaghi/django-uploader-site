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
    template_name = "accounts/login.html"
    @transaction.atomic
    def get_success_url(self):
        messages.success(self.request, 'You were logged in successfully')
        return reverse_lazy('file:home')
# Register view
class Register(AuthMixin,CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    @transaction.atomic
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'You were registered in successfully')
        return redirect('file:home')
    def form_invalid(self, form):
        messages.error(self.request, 'an error occurred while processing your request')
        return redirect('accounts:register')

# Logout view
def Logout(request):
	logout(request) if request.user.is_authenticated else redirect("accounts:register")
	return redirect("accounts:register")

# Set special page
class SetSpecial(SetSpecialMixin,TemplateView):
    template_name = "accounts/SetSpecial.html"
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
