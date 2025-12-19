from django.urls import path 
from . import views

urlpatterns = [path("", views.home, name="Home"),
                path("<int:id>", views.content, name="content"),
                path("create/", views.create, name = "Create"),
                path("showall/", views.showAll, name = "ShowALl"),

                path("greet/<str:welcome>/", views.greet, name = "Welcome"),
                ]