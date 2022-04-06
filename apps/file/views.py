from django.shortcuts import render,redirect
from django.views.generic import View,ListView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
import uuid
from file.models import UserFile
from account.models import User
from .forms import FileForm
from .mixins import UserLimit
# Create your views here.
class Home(LoginRequiredMixin,ListView):
    template_name = "file/Home.html"
    def get_queryset(self):
        object = UserFile.objects.filter(owner=self.request.user)
        return object

class AddFile(LoginRequiredMixin,UserLimit,View):
    template_name = "file/AddFile.html"
    form_class = FileForm
    success_url = "file:home"
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = uuid.uuid4().hex.upper()[0:6]
            form.owner = self.request.user
            form.save()
            User.objects.filter(username=self.request.user.username).update(
                limit= self.request.user.limit - 2
            )
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})