from django.shortcuts import render
from .models import Service, Car, Order, OrderLine

def index(request):
    context = {
        'num_services': Service.objects.count(),
        'num_cars': Car.objects.count(),
        'num_orders_done': Order.objects.filter(status='c').count(),
    }
    return render(request, template_name="index.html", context=context)