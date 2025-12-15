from django.contrib.auth.models import User
from django.db import models

class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    license_plate = models.CharField()
    vin_code = models.CharField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.license_plate})'


class Order(models.Model):
    car = models.ForeignKey(to="Car", on_delete=models.CASCADE, related_name="orders")
    date = models.DateTimeField(auto_now_add=True)

    CHOICES_STATUS = [
        ("p", "Pending"),
        ("i", "In Progress"),
        ("c", "Completed"),
        ("d", "Cancelled"),
    ]

    status = models.CharField(choices=CHOICES_STATUS, default='p')

    def total(self):
        result = 0
        for line in self.lines.all():
            result += line.line_sum()
        return result

    def __str__(self):
        return f'{self.car} ({self.date})'


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, related_name='lines')
    service = models.ForeignKey(to="Service", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def line_sum(self):
        return self.service.price * self.quantity

