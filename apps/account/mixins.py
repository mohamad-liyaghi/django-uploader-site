from django.shortcuts import redirect
#Authentication mixin
class AuthMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("file:home")
        else:
            return super().dispatch(request, *args, **kwargs)