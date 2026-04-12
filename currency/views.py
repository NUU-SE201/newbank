from django.http import HttpResponse, JsonResponse

exchange_rates_data = {
    'usd': 1.0,
    'eur': 0.92,
    'gbp': 0.79,
    'uzs': 12500,
    'kgs': 89.50,
    'kzt': 450.00,
}

def exchange_rates(request):
    return JsonResponse(exchange_rates_data)

def exchange(request):
    from_currency = request.GET.get('from','').lower()
    to_currency = request.GET.get('to','').lower()
    amount = float(request.GET.get('amount', 1))

    if from_currency not in exchange_rates_data or to_currency not in exchange_rates_data:
        return HttpResponse("Invalid currency code, we don't have it yet")
    
    usd_amount = amount / exchange_rates_data[from_currency]    
    converted = usd_amount * exchange_rates_data[to_currency]

    return HttpResponse(
        f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
    )