#views.py
from django.shortcuts import render
from .models import Quote
import random

def home(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes)

    context = {
        'random_quote': random_quote,
    }
    return render(request, 'myapp/home.html', context)