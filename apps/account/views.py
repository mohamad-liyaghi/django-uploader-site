from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
from django.db import transaction
from .forms import RegisterForm
from .mixins import AuthMixin
# Create your views here.
# login view
class Login(AuthMixin,LoginView):
    template_name = "account/login.html"
    @transaction.atomic
    def get_success_url(self):
        messages.success(request, 'You were logged in successfully')
        return reverse_lazy('file:home')
# Register view
class Register(AuthMixin,CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    @transaction.atomic
    def form_valid(self, form):
        form.save()
        messages.success(request, 'You were registered in successfully')
        return redirect('file:home')
    def form_invalid(self, form):
        messages.error(self.request, 'an error occurred while processing your request')
        return redirect('account:register')

# Logout view
def Logout(request):
	logout(request) if request.user.is_authenticated else redirect("account:register")
	return redirect("account:register")
#404 page
def handler404(request,exception):
    return render(request,"404/404.html")