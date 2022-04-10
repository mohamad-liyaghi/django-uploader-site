from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,ListView,DetailView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.http import FileResponse
import uuid
from file.models import UserFile
from account.models import User
from .forms import FileForm
from .mixins import UserLimit
# Create your views here.
# Home page view
class Home(LoginRequiredMixin,ListView):
    template_name = "base/Home.html"
    def get_queryset(self):
        object = UserFile.objects.filter(owner=self.request.user)
        return object
# Add file page view
class AddFile(LoginRequiredMixin,UserLimit,FormView):
    template_name = "file/AddFile.html"
    form_class = FileForm
    success_url = "file:home"
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.slug = uuid.uuid4().hex.upper()[0:6]
        form.owner = self.request.user
        form_file = form.file
        form.save()
        User.objects.filter(username=self.request.user.username).update(
            limit=self.request.user.limit - 1
        )
        return redirect(self.success_url)


# File detail view
class DetailFile(DetailView):
    template_name = "file/DetailFile.html"
    def get_object(self):
        slug = self.kwargs.get('slug')
        object = get_object_or_404(UserFile, slug=slug)
        return object

# File download view
class FileDownload(View):
    def get(self, request,slug, *args, **kwargs):
        object = get_object_or_404(UserFile, slug=slug)
        return FileResponse(object.file, as_attachment=True)

# File delete view
def FileDelete(request, slug):
    model = UserFile.objects.get(slug=slug)
    model.delete()
    User.objects.filter(username=request.user.username).update(limit=request.user.limit + 1)
    return redirect('file:home')