from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency/', include('currency.urls')),
    path('plastic-cards/', include('cards.urls')),
    path('', include('home.urls')), 
    path('booking/', include('booking.urls')),
]