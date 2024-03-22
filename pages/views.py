from django.shortcuts import render, get_object_or_404
from shared.models import Settings
from banner.models import Banner
from client_feedback.models import Feedback
from tools.models import Tools
from products.models import Product

def about(requests):

    filtered_banners = Banner.objects.filter(page_url = '/about-us', about = 'About us', banner_type = 'Footer').all()
    hero_banner = Banner.objects.filter(page_url = '/about-us', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    social_links = Settings.objects.latest('created_at')
    return render (requests, "about.html", {'social_links': social_links, 'hero_banners': hero_banner, 'filtered_banners': filtered_banners})

def index(requests):

    feedbacks = Feedback.objects.all()
    call_to_action_banner = Banner.objects.filter(page_url = '/index', about = 'Call to action').latest('created_at')
    hero_banner = Banner.objects.filter(page_url = '/index', about = 'Hero banner').latest('created_at')
    about_banner = Banner.objects.filter(page_url = '/index', about = 'About us').latest('created_at')
    social_links = Settings.objects.latest('created_at')
    return render (requests, "index.html", {'social_links': social_links, 'about_banner': about_banner, 'feedbacks': feedbacks, 'hero_banner': hero_banner, 'call_to_action_banner': call_to_action_banner})

def services(requests):

    hero_banner = Banner.objects.filter(page_url = '/services', about = 'Hero banner').latest('created_at')
    trainings = Banner.objects.filter(page_url = '/services', about = 'Trainings').latest('created_at')
    tools = Banner.objects.filter(page_url = '/services', about = 'Tools').latest('created_at') 
    patents = Banner.objects.filter(page_url = '/services', about = 'Patents').latest('created_at')
    document_library = Banner.objects.filter(page_url = '/services', about = 'Document library').latest('created_at')
    capabilities = Banner.objects.filter(page_url = '/services', about = 'Capabilities').latest('created_at')
    brands = Banner.objects.filter(page_url = '/services', about = 'Brands').latest('created_at')
    social_links = Settings.objects.latest('created_at')
    return render (requests, "services.html", {'social_links': social_links, 'brands': brands, 'capabilities': capabilities, 'document_library': document_library, 'patents': patents, 'tools': tools, 'trainings': trainings, 'hero_banner': hero_banner})

def tools(requests):
    
    tools = Tools.objects.all()
    products = Product.objects.select_related('tool').all()
    social_links = Settings.objects.latest('created_at')
    return render (requests, "tools.html", {'social_links': social_links, 'tools': tools, 'products': products})

def products(requests, product_id):
    
    product = get_object_or_404(Product, pk = product_id)
    social_links = Settings.objects.latest('created_at')
    return render (requests, "products.html", {'social_links': social_links, 'product': product})
