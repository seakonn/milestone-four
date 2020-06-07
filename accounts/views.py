from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from commissions.models import Commission

"""
********************************************************************

ORIGINAL CODE IN THIS FILE COPIED FROM:

https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/accounts

********************************************************************
"""


@login_required
def logout(request):
    """Logs the user out and brings them to the home page"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home'))


def login(request):
    """Renders the login page and authenticates users"""
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page and process new registrations"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """Shows the status of commissions the user has ordered"""

    # get commissions specific to the current user
    commissions = Commission.objects.filter(owner=request.user)

    return render(request, 'profile.html', {"commissions": commissions})
