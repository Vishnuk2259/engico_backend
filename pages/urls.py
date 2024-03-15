from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'Index'),
    path('about-us/', views.about, name = 'About Us'),
    path('services/', views.services, name = 'Services'),
    path('tools/', views.tools, name = 'Tools'),

]