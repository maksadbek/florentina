from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^create/', views.create, name='create'),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^profile/', views.user, name='profile'),
    url(r'^login/', views.auth, name='login'),
    url(r'^logout/', views.signout, name='logout'),
]
