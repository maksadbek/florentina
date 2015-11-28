from django import template
from flowers.models import Category
register = template.Library()
@register.inclusion_tag('_partials/nav.html')
def show_categories():
    categories = Category.objects.all()
    print categories
    return {'categories':categories}
