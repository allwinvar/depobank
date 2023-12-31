"""
URL configuration for DreamzBank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.logout, name='logout'),
    path('account/apply',views.apply,name='apply'),
    path('account/dashboard/',views.dashboard,name='dashboard'),

    #some less important
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('gallery/', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),

]