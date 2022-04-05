from django.shortcuts import render
from django.views.generic import ListView
from file.models import UserFile
# Create your views here.
class Home(ListView):
    template_name = "file/Home.html"
    def get_queryset(self):
        pass

