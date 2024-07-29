from django.contrib import admin

# Register your models here.
from .models import Customer, Reservation

admin.site.register(Customer)
admin.site.register(Reservation)
