from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Customer(models.Model):
    """
    Class to manage customers.
    """
    name = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(unique=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Reservation(models.Model):
    """
    Class to manage reservations.
    """
    reservation_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_duration = models.DurationField()
    reservation_size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    reservation_booked_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)

