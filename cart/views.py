from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from flowers.models import Flower, Size
from cart import utils

def show(request):
    cart =  utils.get_cart_items(request)
    context = {'cart':cart}
    return render(request, 'cart/show.html', context)

def add(request):
    utils.add_to_cart(request)
    count = utils.count_cart_items(request)
    context = {'cart_items': count}
    return JsonResponse(context)

def remove(request):
    postdata = request.POST.copy()
    product_id = postdata['product_id']
    item = utils.get_single_item(request, product_id)
    if item:
        item.delete()
    count = utils.count_cart_items(request)
    context = {'cart_items': count}
    return JsonResponse(context)
