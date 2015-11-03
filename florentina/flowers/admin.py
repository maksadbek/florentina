from django.contrib import admin

from .models import Flower
from .models import Category

admin.site.register(Flower)
admin.site.register(Category)
