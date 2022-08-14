from django.shortcuts import redirect

class LimitMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.limit > 0:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("file:home")
