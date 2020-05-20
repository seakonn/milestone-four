from django.shortcuts import render

# Create your views here.


def home(request):
    """Return the home.html file"""
    return render(request,  'home.html')


def request_commission(request):
    """ Returns the request commission page """

    return render(request, 'request.html')
