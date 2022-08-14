from django.urls import path
from .views import FileList, AddFile, DetailFile, FileDownload, FileDelete

app_name = "file"

urlpatterns = [
    path("", FileList.as_view(), name= "file-list"),
    path('add/',AddFile.as_view(),name="add-file"),
    path("detail/<int:id>/<str:slug>/", DetailFile.as_view(), name="file-detail"),
    path("download/<str:slug>/",FileDownload.as_view(),name="download-file"),
    path("delete/<str:slug>/",FileDelete,name="delete-file")
]