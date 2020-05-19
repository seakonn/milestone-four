from django.shortcuts import render

# Create your views here.


def home(request):
    """Return the home.html file"""
    return render(request,  'home.html')
