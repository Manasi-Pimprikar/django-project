from django.shortcuts import render
from carapp import models
from .models import car,owner,order

# Create your views here.

def data(request):
    data =order.objects.all()
    return render(request, 'car.html',locals()) 