from django.shortcuts import redirect
class UserLimit():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.limit > 0 or self.request.is_special:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("file:home")
