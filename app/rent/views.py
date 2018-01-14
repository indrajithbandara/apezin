from django.shortcuts import render, HttpResponse
from app.rent.models import Apartment


def apartments(request):
    template = 'rent/index.html'

    if request.method == 'GET':
        data = {
            'apartments': Apartment.objects.all()
        }
        return render(request, template, context=data)
