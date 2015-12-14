from django import template
from cart import utils
register = template.Library()
@register.simple_tag
def cart_count(session_key):
    cart_count = utils.count_cart_items_by_session_key(session_key)
    print cart_count
    return cart_count
