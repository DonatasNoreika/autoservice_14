from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
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


class ServiceListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Service
    template_name = "services.html"
    context_object_name = "services"

    def test_func(self):
        return self.request.user.is_staff


class ServiceCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Service
    template_name = "form.html"
    fields = ['name', 'price']
    success_url = reverse_lazy('services')

    def test_func(self):
        return self.request.user.is_staff


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Service
    template_name = "form.html"
    fields = ['name', 'price']
    success_url = reverse_lazy('services')

    def test_func(self):
        return self.request.user.is_staff


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Service
    template_name = "service_delete.html"
    context_object_name = "service"
    success_url = reverse_lazy('services')

    def test_func(self):
        return self.request.user.is_staff


class CarListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def test_func(self):
        return self.request.user.is_staff


class CarDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Car
    template_name = "car.html"
    context_object_name = "car"

    def test_func(self):
        return self.request.user.is_staff


class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Car
    template_name = "form.html"
    fields = ['make', 'model', 'owner', 'license_plate', 'vin_code']
    success_url = reverse_lazy('cars')

    def test_func(self):
        return self.request.user.is_staff

class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Car
    template_name = "form.html"
    fields = ['make', 'model', 'owner', 'license_plate', 'vin_code']

    def get_success_url(self):
        return reverse("car", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Car
    template_name = "car_delete.html"
    context_object_name = "car"
    success_url = reverse_lazy('cars')

    def test_func(self):
        return self.request.user.is_staff


class OrderListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"

    def test_func(self):
        return self.request.user.is_staff


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"

    def test_func(self):
        return self.request.user.is_staff


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Order
    template_name = "form.html"
    fields = ['car', 'status']

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    template_name = "form.html"
    fields = ['car', 'status']

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Order
    template_name = "order_delete.html"
    context_object_name = "order"
    success_url = reverse_lazy('orders')

    def test_func(self):
        return self.request.user.is_staff


class OrderLineCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = OrderLine
    template_name = "form.html"
    fields = ['service', 'quantity']

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.order.pk})

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class OrderLineUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = OrderLine
    template_name = "form.html"
    fields = ['service', 'quantity']

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.order.pk})

    def test_func(self):
        return self.request.user.is_staff


class OrderLineDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = OrderLine
    template_name = "line_delete.html"
    context_object_name = "line"

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.order.pk})

    def test_func(self):
        return self.request.user.is_staff