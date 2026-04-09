from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Booking

def index(request):
    bookings = Booking.objects.all()
    my_booking = request.session.get('my_booking', None)
    return render(request,
                'booking/index.html',
                {'bookings': bookings,
                'my_booking': my_booking})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            new_booking = Booking(name=name)
            new_booking.save()
            request.session['my_booking'] = new_booking.id
        return HttpResponseRedirect(reverse('booking:index'))
    return render(request, 'booking/add.html')
