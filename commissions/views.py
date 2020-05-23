from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommissionForm
from .models import Commission, CommissionType

# Create your views here.


def home(request):
    """Return the home.html file"""
    return render(request,  'home.html')


def request_commission(request):
    """ Returns the request commission page """

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
            return redirect(home)
    else:
        form = CommissionForm()

    return render(request, 'request.html',
                  {'form': form, 'comm_types': comm_types})


def display_commission(request, id):
    """ Displays the requested commission page """

    the_commission = get_object_or_404(Commission, pk=id)

    return render(request, 'commission.html', {'commission': the_commission})
