from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usercars/", views.UserCarListView.as_view(), name="usercars"),
    path("usercars/<int:pk>/", views.UserCarDetailView.as_view(), name="usercar"),
    path("userorders/<int:pk>/", views.UserOrderDetailView.as_view(), name="userorder"),
    path("services/", views.ServiceListView.as_view(), name="services"),
    path("services/create/", views.ServiceCreateView.as_view(), name="service_create"),
]
