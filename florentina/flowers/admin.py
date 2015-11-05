from django.contrib import admin

from .models import Flower
from .models import Category
from .models import Type

admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Type)
