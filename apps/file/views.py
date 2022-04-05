from django.shortcuts import render,redirect
from django.views.generic import View,ListView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from .forms import FileForm
from file.models import UserFile
# Create your views here.
class Home(LoginRequiredMixin,ListView):
    template_name = "file/Home.html"
    def get_queryset(self):
        pass

class AddFile(View):
    template_name = "file/AddFile.html"
    form_class = FileForm
    success_url = "file:home"
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = uuid.uuid4().hex.upper()[0:6]
            form.owner = self.request.user
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})