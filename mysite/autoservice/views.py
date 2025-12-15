from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views import generic
from .models import Service, Car, Order, OrderLine

def index(request):
    context = {
        'num_services': Service.objects.count(),
        'num_cars': Car.objects.count(),
        'num_orders_done': Order.objects.filter(status='c').count(),
    }
    return render(request, template_name="index.html", context=context)


class UserCarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "usercars.html"
    context_object_name = "cars"

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)


class UserCarDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Car
    template_name = "usercar.html"
    context_object_name = "car"

    def test_func(self):
        return self.get_object().owner == self.request.user


class UserOrderDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Order
    template_name = "userorder.html"
    context_object_name = "order"

    def test_func(self):
        return self.get_object().car.owner == self.request.user