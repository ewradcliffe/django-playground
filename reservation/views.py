from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import Reservation

# Create your views here.
#def my_reservations(request):
 #   return HttpResponse("Hello reservations!")

class ReservationList(generic.ListView):
    #model = Reservation
    queryset = Reservation.objects.all()
    template_name = "reservation_list.html"


    