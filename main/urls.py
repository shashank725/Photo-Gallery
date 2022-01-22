from unicodedata import name
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('', views.homePage, name="homepage"),
    path('<pk>/', views.detail, name="detail"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
