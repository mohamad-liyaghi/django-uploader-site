from django.shortcuts import redirect, get_object_or_404
from django.views.generic import  TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .mixins import SetSpecialMixin
from file.models import User



# Set special page
class SetSpecial(LoginRequiredMixin, SetSpecialMixin, TemplateView):
    '''
        Promote a user as special user
    '''
    template_name = "account/SetSpecial.html"
    def get(self,request):
        user = get_object_or_404(User, email= self.request.user.email, id= self.request.user.id)
        user.is_special = True
        user.limit = 50
        user.save()
        messages.success(self.request, 'from now on, you are a special user')
        return redirect("file:home")


#404 page
def handler404(request,exception):
    return render(request,"404/404.html")
