from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usercars/", views.UserCarListView.as_view(), name="usercars"),
]
