from django.urls import path
from .views import Home,AddFile
app_name = "file"
urlpatterns = [
    path("",Home.as_view(),name= "home"),
    path('add/',AddFile.as_view(),name="add-file")
]