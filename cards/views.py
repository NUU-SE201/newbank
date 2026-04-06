from django.shortcuts import render
from django.http import HttpResponseNotFound

supported_cards = [
    "Uzcard",
    "Humo",
    "Visa",
    "MasterCard",
    "UnionPay",
    "Mir",
]

# Create your views here.
def index(request):
    return render(request, 'cards/index.html', {'cards': supported_cards})

def card_info(request, card_name):
    if card_name in supported_cards:
        return render(request, 'cards/card_info.html', {'card_name': card_name})
    else:
        return HttpResponseNotFound("Card not found")