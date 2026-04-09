from django.urls import path
from . import views

app_name = 'currency'
urlpatterns = [
    path('', views.index, name='index'),
    path('exchange/', views.exchange, name='exchange'),
]