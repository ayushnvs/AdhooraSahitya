"""adhoorasahitya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home.views import home_page, base_page, about_page, blog_page, page_not_found

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('base/', base_page, name='base'),
    path('sorry-not-found/', page_not_found, name='404'),
    path('about/', about_page, name='about'),
    path('<str:id>/<str:blog_title>/', blog_page, name='blog'),
]
