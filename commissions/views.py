from django.shortcuts import render
from .forms import CommissionForm

# Create your views here.


def home(request):
    """Return the home.html file"""
    return render(request,  'home.html')


def request_commission(request):
    """ Returns the request commission page """

    form = CommissionForm()

    return render(request, 'request.html', {'form': form})
