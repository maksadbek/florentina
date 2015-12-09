from django.shortcuts import render, get_object_or_404, redirect
from cart.models import CartItem
from django.http import JsonResponse
from flowers.models import Flower, Size
import decimal
import random

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY) == None:
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id 

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    postdata = request.POST.copy()
    product_id = postdata.get('product_id')
    quantity = postdata.get('quantity', 1)
    size_id = postdata.get('size_id', 1)
    p = get_object_or_404(Flower, id=product_id)
    s = get_object_or_404(Size, id=size_id)
    products = get_cart_items(request)
    in_cart = False
    for item in products:
        if item.product.id == p.id and item.size.id == s.id:
            item.augment_quantity(quantity)
            in_cart = True
    if not in_cart:
        item = CartItem()
        item.product = p
        item.quantity = quantity
        item.cart_id = _cart_id(request)
        item.size = s
        item.save()

def count_cart_items(request):
    return get_cart_items(request).count()
            
def get_single_item(request, product_id):
    return get_object_or_404(
            CartItem, 
            id=product_id,
            cart_id=_cart_id(request))

def show(request):
    cart =  get_cart_items(request)
    context = {'cart':cart}
    return render(request, 'cart/show.html', context)

def add(request):
    add_to_cart(request)
    count = count_cart_items(request)
    context = {'cart_items': count}
    return JsonResponse(context)

def remove(request):
    postdata = request.POST.copy()
    print postdata
    product_id = postdata['product_id']
    item = get_single_item(request, product_id)
    if item:
        item.delete()
    context = {'cart_items': count}
    return JsonResponse(context)
