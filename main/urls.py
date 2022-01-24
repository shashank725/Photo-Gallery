from unicodedata import name
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('', views.homePage, name="homepage"),
    path('add/', views.add, name="add"),
    path('gallery/<pk>/', views.detail, name="detail"),
    path('search/', views.search, name="search")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)