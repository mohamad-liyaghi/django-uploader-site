from django.urls import path
from .views import SetSpecial

app_name = "account"

urlpatterns = [
    path("set-special/",SetSpecial.as_view(),name="set-special")
]