from django.contrib import admin
from .models import Service, Car, Order, OrderLine

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class CarAdmin(admin.ModelAdmin):
    list_display = ['owner', 'make', 'model', 'license_plate', 'vin_code']
    list_filter = ['owner', 'make', 'model']
    search_fields = ['license_plate', 'vin_code']

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date', 'status']
    inlines = [OrderLineInLine]

admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)