from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usercars/", views.UserCarListView.as_view(), name="usercars"),
    path("usercars/<int:pk>/", views.UserCarDetailView.as_view(), name="usercar"),
    path("userorders/<int:pk>/", views.UserOrderDetailView.as_view(), name="userorder"),
    path("services/", views.ServiceListView.as_view(), name="services"),
    path("services/create/", views.ServiceCreateView.as_view(), name="service_create"),
    path("services/<int:pk>/update/", views.ServiceUpdateView.as_view(), name="service_update"),
    path("services/<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="service_delete"),
    path("cars/", views.CarListView.as_view(), name="cars"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car"),
    path("cars/create/", views.CarCreateView.as_view(), name="car_create"),
    path("cars/<int:pk>/update/", views.CarUpdateView.as_view(), name="car_update"),
    path("cars/<int:pk>/delete/", views.CarDeleteView.as_view(), name="car_delete"),
    path("orders/", views.OrderListView.as_view(), name="orders"),
]
