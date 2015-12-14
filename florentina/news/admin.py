from django.contrib import admin

from .models import News

from django import forms
from redactor.widgets import RedactorEditor

admin.site.register(News)