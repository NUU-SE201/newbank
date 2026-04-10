from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Booking
bookings = []

def index(request):
    bookings = Booking.objects.all()
    last_booking = request.session.get('last_booking')

    return render(request, 'booking/index.html', {
        'bookings': bookings,
        'last_booking': last_booking
    })

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            new_booking = Booking(name=name)
            new_booking.save()

            # 👇 name emas, ID saqlaymiz
            request.session['last_booking'] = new_booking.id

            return HttpResponseRedirect('/booking/')
    
    return render(request, 'booking/add.html')