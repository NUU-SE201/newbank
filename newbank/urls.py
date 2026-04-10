from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),   # 👈 ENG MUHIM
    path('cards/', include('cards.urls')),
    path('currency/', include('currency.urls')),
    path('booking/', include('booking.urls')),
]