from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('<str:card_name>/', views.card_detail, name='card_detail'),
]