from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("createAccount/", views.register, name="Register"),
    path("", include("django.contrib.auth.urls")),
    path("profile/", views.AccountInfo, name="profile"),
]