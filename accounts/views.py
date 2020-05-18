from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.


def index(request):
    """ Returns the homepage """

    return render(request, "test.html")


def logout(request):
    """ Logs the user out """

    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")

    return redirect(reverse('index'))


def login(request):
    """ Logs the user in """
    login_form = UserLoginForm()

    return render(request, 'login.html', {"login_form": login_form})
