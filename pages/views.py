from django.shortcuts import render
from shared.models import Settings

def about(requests):

    social_links = Settings.objects.latest('created_at')
    return render (requests, "about.html", {'social_links' : social_links})

def index(requests):

    social_links = Settings.objects.latest('created_at')
    return render (requests, "index.html", {'social_links' : social_links})

def services(requests):

    social_links = Settings.objects.latest('created_at')
    return render (requests, "services.html", {'social_links' : social_links})

def tools(requests):
    
    social_links = Settings.objects.latest('created_at')
    return render (requests, "tools.html", {'social_links' : social_links})
