"""Aurora URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from core.views import contact_form_submit, subscribe_newsletter

# Görünüm fonksiyonları
def index(request):
    return render(request, 'index.html')

def pagina(request):
    return render(request, 'pagina.html')

urlpatterns = [
    path('', pagina),
    path('pagina/', pagina),
    path('en/', index),
    path('en/index', index),
    path('admin/', admin.site.urls),
    path('subscribe/', subscribe_newsletter, name='subscribe'),
    path('contact-submit/', contact_form_submit, name='contact_submit'),
]

# Medya dosyaları (görsel upload için)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
