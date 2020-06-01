from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommissionForm
from .models import Commission, CommissionType
from accounts.views import user_profile

# Create your views here.


def home(request):
    """Return the home page"""
    return render(request,  'home.html')


def request_commission(request):
    """
    Returns the request commission page and processes any
    commission information posted by the user
    """

    comm_types = CommissionType.objects.all()

    if request.method == "POST":

        form = CommissionForm(request.POST, request.FILES)

        if form.is_valid():

            # want to add current logged in user as registering the commission
            temp = form.save(commit=False)
            temp.owner = request.user

            # want to associate commission with the uploaded commission type
            temp.type = comm_types.get(type_name=request.POST['ctypes'])

            form.save()
            return redirect(user_profile)
    else:
        form = CommissionForm()

    return render(request, 'request.html',
                  {'form': form, 'comm_types': comm_types})


def display_commission(request, id):
    """ Displays a specific commission page from its id """

    commission = get_object_or_404(Commission, pk=id)

    return render(request, 'commission.html', {'commission': commission})
