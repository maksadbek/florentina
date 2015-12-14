from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^add/', views.add, name='add'),
    url(r'^remove/', views.remove, name='remove'),
]
