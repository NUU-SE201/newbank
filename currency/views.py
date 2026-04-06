from django.shortcuts import render
from django.http import HttpResponseNotFound

currencies = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "UZS": 12200.0,
    "JPY": 110.0,
    "KRW": 1150.0,
}

# Create your views here.
def index(request):
    return render(request, 'currency/index.html', 
                  {'currencies': currencies})

def exchange(request):
    from_currency = request.GET.get('from', '').upper()
    to_currency = request.GET.get('to', '').upper()
    if from_currency not in currencies or to_currency not in currencies:
        return HttpResponseNotFound("Currency not supported.")

    exchange_rate = currencies[to_currency] / currencies[from_currency]
    return render(request, 'currency/exchange.html',
                  {'from': from_currency,
                   'to': to_currency,
                   'rate': exchange_rate})