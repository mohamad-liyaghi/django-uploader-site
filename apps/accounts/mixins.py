from django.shortcuts import redirect


class SetSpecialMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_special:
            return redirect("file:home")
        else:
            return super().dispatch(request, *args, **kwargs)