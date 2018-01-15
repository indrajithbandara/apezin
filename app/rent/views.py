from django.shortcuts import render, redirect
from app.rent.models import Apartment
from app.rent.forms import AddApartmentForm


def apartments(request):
    template = 'rent/index.html'

    form = AddApartmentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    data = {
        'apartments': Apartment.objects.all(),
        'form_apartment': form
    }

    return render(request, template, context=data)
