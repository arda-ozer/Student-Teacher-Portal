from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin paneli için
    path('', include('school.urls')),  # school uygulamasının URL'leri
]