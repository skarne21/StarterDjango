from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/account/login/") # Redirect to login after successful signup
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def AccountInfo(response):
    if response.user.is_authenticated:
        # Show them their info instead of logging them out immediately
        return render(response, "registration/accountInfo.html", {"user": response.user})
    else:
        return redirect("login") # Use the named URL from auth.urls


# Create your views here.
