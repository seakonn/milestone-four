from django.shortcuts import render, redirect
from .forms import CommissionForm

# Create your views here.


def home(request):
    """Return the home.html file"""
    return render(request,  'home.html')


def request_commission(request):
    """ Returns the request commission page """

    if request.method == "POST":

        form = CommissionForm(request.POST, request.FILES)

        if form.is_valid():

            # want to add current logged in user as registering the commission
            temp = form.save(commit=False)
            temp.owner = request.user
            form.save()
            return redirect(home)
    else:
        form = CommissionForm()

    return render(request, 'request.html', {'form': form})
