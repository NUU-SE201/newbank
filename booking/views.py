from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Booking

# Create your views here.

@login_required(login_url='accounts:login')
def index(request):
    bookings = Booking.objects.filter(booked_by=request.user)
    return render(request, 'booking/index.html', {'bookings': bookings})

@login_required(login_url='accounts:login')
def add(request):
    if request.method == 'POST':
        reason = request.POST.get('reason', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        
        if reason and date and time:
            user = request.user
            booking = Booking(reason=reason, date=date, time=time, booked_by=user)
            booking.save()
            return HttpResponseRedirect(reverse('booking:index'))
        else:
            return render(request, 'booking/add.html', {'error_message': 'All fields are required.'})
            
    return render(request, 'booking/add.html')