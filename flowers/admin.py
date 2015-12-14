from django.contrib import admin

from .models import Flower
from .models import Category
from .models import Type
from .models import Size

from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm as OldFlatpageForm
 
from django import forms
from redactor.widgets import RedactorEditor
 
class FlatpageForm(OldFlatpageForm):
    #content = forms.CharField(widget=RedactorEditor())
    class Meta:
        model = FlatPage
        widgets = {
           'content': RedactorEditor(),
        }
        fields = "__all__"
 
class FlatPageAdmin(OldFlatPageAdmin):
    form = FlatpageForm
 
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Size)
