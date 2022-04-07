from django.urls import path
from .views import Home,AddFile,DetailFile
app_name = "file"
urlpatterns = [
    path("",Home.as_view(),name= "home"),
    path('add/',AddFile.as_view(),name="add-file"),
    path("detail/<str:slug>/",DetailFile.as_view(),name="detail-file")
]