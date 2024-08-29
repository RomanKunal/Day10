from django.shortcuts import render
from .models import Person

def fetch(request):
    # Fetch all persons whose name starts with 'A'
    persons = Person.objects.filter(name__startswith='A')
    return render(request, 'index.html', {'persons': persons})

def fetch2(request):
    persons = Person.objects.filter(name__regex=r'^..s')
    return render(request, 'index.html', {'persons': persons})