from django.shortcuts import render  # this defines the render function
from django.http import HttpResponseRedirect
from django.urls import reverse

bookings = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
]

def index(request):
    return render(request, 'booking/index.html', {'bookings': bookings})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            new_id = len(bookings) + 1
            bookings.append({'id': new_id, 'name': name})
            request.session['my_booking'] = new_id
        return HttpResponseRedirect(reverse('booking:index'))
    return render(request, 'booking/add.html')