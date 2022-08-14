from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import FileResponse
from django.utils.text import slugify

from file.models import UserFile
from accounts.models import User
from .forms import FileForm
from .mixins import LimitMixin

class FileList(LoginRequiredMixin, ListView):
    '''A list of all uploaded files from a user'''
    template_name = "file/list.html"
    context_object_name = "files"

    def get_queryset(self):
        object = UserFile.objects.filter(owner= self.request.user)
        return object


class AddFile(LoginRequiredMixin, LimitMixin, FormView):
    '''Add a new file'''
    template_name = "file/add.html"
    form_class = FileForm
    success_url = "file:file-list"

    @transaction.atomic()
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)

        form.slug = slugify(form.title)
        form.owner = self.request.user

        if self.request.user.is_special and form.file.size < 10485760:
                self.request.user.limit = self.request.user.limit - 1
                self.request.user.save()
                form.save()
                return redirect(self.success_url)

        if form.file.size < 5242880 :
                self.request.user.limit = self.request.user.limit - 1
                self.request.user.save()
                form.save()
                return redirect(self.success_url)

        return redirect(self.success_url)


class DetailFile(DetailView):
    '''Detail page of a file'''
    template_name = "file/detail.html"

    def get_object(self):
        object = get_object_or_404(UserFile, id=self.kwargs["id"], slug=self.kwargs["slug"])
        ip_address = self.request.user.ip_address
        # add ip to the views
        if ip_address not in object.views.all():
            object.views.add(ip_address)

        return object

# File download view
class FileDownload(View):
    def get(self, request, id, slug, *args, **kwargs):
        object = get_object_or_404(UserFile, id= id, slug=slug)
        return FileResponse(object.file, as_attachment=True)

# File delete view
@transaction.atomic()
def DeleteFile(request, id, slug):
    object = get_object_or_404(UserFile, id= id, slug= slug, owner= request.user)
    object.delete()
    request.user.limit = request.user.limit + 1
    request.user.save()
    return redirect('file:file-list')