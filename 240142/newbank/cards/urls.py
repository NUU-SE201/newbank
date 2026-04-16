from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:card_name>/', views.card_info, name='card_info'),
]