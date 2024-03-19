from django.shortcuts import render
from shared.models import Settings
from banner.models import Banner
from django.urls import reverse

def about(requests):

    filtered_banners = Banner.objects.filter(page_url = '/about-us', about = 'about us', banner_type = 'Footer').all()
    banners = Banner.objects.filter(page_url = '/about-us', about = 'about us', banner_type = 'Header').latest('created_at')
    social_links = Settings.objects.latest('created_at')
    return render (requests, "about.html", {'social_links': social_links, 'banners': banners, 'filtered_banners': filtered_banners})

def index(requests):

    banner = Banner.objects.filter(page_url = '/index').latest('created_at')
    social_links = Settings.objects.latest('created_at')
    return render (requests, "index.html", {'social_links': social_links, 'banner': banner})

def services(requests):

    trainings = Banner.objects.filter(page_url = '/services', about = 'Trainings').latest('created_at')
    tools = Banner.objects.filter(page_url = '/services', about = 'Tools').latest('created_at') 
    patents = Banner.objects.filter(page_url = '/services', about = 'Patents').latest('created_at')
    document_library = Banner.objects.filter(page_url = '/services', about = 'Document library').latest('created_at')
    capabilities = Banner.objects.filter(page_url = '/services', about = 'Capabilities').latest('created_at')
    brands = Banner.objects.filter(page_url = '/services', about = 'Brands').latest('created_at')
    social_links = Settings.objects.latest('created_at')
    return render (requests, "services.html", {'social_links': social_links, 'brands': brands, 'capabilities': capabilities, 'document_library': document_library, 'patents': patents, 'tools': tools, 'trainings': trainings})

def tools(requests):
    
    social_links = Settings.objects.latest('created_at')
    return render (requests, "tools.html", {'social_links': social_links})
