"""
URL configuration for Cara project.

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
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'index'),
    
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    
    path('register/', views.register, name = 'register'), 
    path('shop/', views.shop, name = 'shop'),
    path('blog/', views.blog, name = 'blog'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('cart/', views.cart, name = 'cart'),
    
    path('add2cart/<int:pk>/', views.addToCart, name='add2cart'),
    path('remove/<int:pk>/', views.removeFromCart, name='remove'),
    path('product/<slug:slug>/', views.details, name='sproduct'),
]
