"""florentina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

import flowers.views as flowers_views

urlpatterns = [
    url(r'^$', flowers_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flowers/', include('flowers.urls', namespace='flowers')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^favourites/', include('favourites.urls', namespace='favourites')),
    url(r'^redactor/', include('redactor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)