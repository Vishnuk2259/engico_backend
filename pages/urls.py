from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about-us/', views.about, name = 'about-us'),
    path('services/', views.services, name = 'services'),
    path('tools/', views.tools, name = 'tools'),

]