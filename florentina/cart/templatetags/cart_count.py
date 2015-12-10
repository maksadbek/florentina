from django import template
from cart import utils
register = template.Library()
@register.inclusion_tag('_partials/header.html')
def cart_count(request):
    print "----------", request
    cart_count = utils.get_cart_items(request)
    return {'cart_count': cart_count}
