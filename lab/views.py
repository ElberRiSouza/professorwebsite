from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def skills(request):
    return render(request, 'skills.html', {})

def publications(request):
    return render(request, 'publications.html', {})

def news(request):
    return render(request, 'news.html', {})

def booking(request):
    return render(request, 'booking-system.html', {})

def team(request):
    return render(request, 'team.html', {})

def research(request):
    return render(request, 'research.html', {})

def contact(request):
    return render(request, 'contact.html', {})