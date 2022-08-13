from django.urls import path
from .views import Login,Register,Logout,SetSpecial
app_name = "accounts"
urlpatterns = [
    path("login/",Login.as_view(),name="login"),
    path('register/',Register.as_view(),name="register"),
    path("logout/",Logout,name="logout"),
    path("set-special/",SetSpecial.as_view(),name="set-special")
]