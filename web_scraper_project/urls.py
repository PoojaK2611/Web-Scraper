"""
web_scraper_project URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scrapingsite/',include('web_scraper_tool.urls'))
]
