from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<id>[0-9]+)/types/', views.category_types, name='category_types'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
