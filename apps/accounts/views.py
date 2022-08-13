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
