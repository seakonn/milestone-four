from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.


def index(request):
    """ Returns the homepage """

    return render(request, "test.html")

def logout(request):
    """ Logs the user out """

    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")

    return redirect(reverse('index'))