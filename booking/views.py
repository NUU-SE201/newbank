from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Booking

bookings = [
    {'id': 1,'name': 'Alice'},
    {'id': 2,'name': 'Bob'},
    {'id': 3,'name': 'Dave'},
]
# Create your views here.
def index(request):
    my_booking = request.session.get('my_booking', None)
    bookings = Booking.objects.all().order_by('id')
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