from django.shortcuts import render
from .models import PersonPerson as Person
from django.db.models import Avg


def fetch(request):
    # Fetch all persons whose name starts with 'A'
    persons = Person.objects.filter(name__startswith='A')
    return render(request, 'index.html', {'persons': persons})

def fetch2(request):
    persons = Person.objects.filter(name__regex=r'^..s')
    return render(request, 'index.html', {'persons': persons})

def fetch3(request):
    persons=Person.objects.filter(salary__gt=50000)
    return render(request, 'fetch3.html', {'persons': persons})

def fetch4(request):
    avg_salary = Person.objects.all().aggregate(Avg('salary'))['salary__avg']
    persons = Person.objects.all()
    return render(request, 'result.html', {'persons': persons, 'avg_salary': avg_salary})

def fetch5(request):
    persons = Person.objects.all().order_by('salary')
    return render(request, 'fetch5.html', {'persons': persons})