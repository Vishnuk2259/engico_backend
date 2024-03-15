from django.shortcuts import render

def about(requests):
    
    return render (requests, "about.html")

def index(requests):

    return render (requests, "index.html")

def services(requests):

    return render (requests, "services.html")

def tools(requests):

    return render (requests, "tools.html")
