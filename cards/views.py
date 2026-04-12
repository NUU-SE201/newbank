from django.http import HttpResponse

cards_data = {
    'humo': {
        'name': 'HUMO',
        'description': 'Local payment card used in Uzbekistan.'
    },
    'uzcard': {
        'name': 'UzCard',
        'description': 'Popular local card for daily payments.'
    },
    'visa': {
        'name': 'Visa',
        'description': 'International payment card.'
    },
}

def card_list(request):
    html = """
    <h1>Plastic Card Types</h1>
    <ul>
        <li><a href="/plastic-cards/humo/">HUMO</a></li>
        <li><a href="/plastic-cards/uzcard/">UzCard</a></li>
        <li><a href="/plastic-cards/visa/">Visa</a></li>
    </ul>
    """
    return HttpResponse(html)

def card_detail(request, card_name):
    card = cards_data.get(card_name.lower())

    if not card:
        return HttpResponse("Card not found")

    html = f"""
    <h1>{card['name']}</h1>
    <p>{card['description']}</p>
    <a href="/plastic-cards/">Back to all cards</a>
    """
    return HttpResponse(html)