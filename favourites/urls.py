from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^new/', views.new, name='new'),
    url(r'^(?P<id>[0-9]+)/delete/', views.delete, name='delete'),
]
