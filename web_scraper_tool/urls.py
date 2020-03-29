from django.urls import path
from . import views

app_name = 'web_scraper'

urlpatterns = [
    path('home/', views.web_scraper, name='home')
]
