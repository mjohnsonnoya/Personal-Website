from .models import Quote
import random

def random_quote(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes)
    return {'random_quote': random_quote}
