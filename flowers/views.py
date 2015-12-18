# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Flower
from .models import Category
from news.models import News

def index(request):
    category_name = request.GET.get('category','')
    sorting = request.GET.get('sorting', '')
    flowers = Flower.objects.order_by('category')
    news = News.objects.order_by('date')[:1]
    # if category is not given, then show all
    if category_name == "":
        context = {'flowers':flowers, 'news':news}
        return render(request, 'flowers/index.html', context)
    # if category is given, filter by category and sort by popularity by default
    if sorting not in ["popularity", "created"]:
        sorting = "popularity"

    context = { 
        'sorting': sorting, 
        'category':category_name,
        'flowers':flowers.filter(category__name=category_name).order_by("-"+sorting) ,
    }
    return render(request, 'flowers/catalog.html', context)

def detail(request, id):
    flower = get_object_or_404(Flower, id=id)
    if not request.user.is_anonymous():
        request.user.lastSeenProducts.add(flower)
    flowers = Flower.objects.filter(category=flower.category).exclude(id=id).order_by('?')[:4]
    context = {'flower':flower, 'flowers':flowers}
    return render(request, 'flowers/detail.html', context)

def category_types(request, id):
    category = get_object_or_404(Category,id=id)
    types = category.type.all()
    response =  serializers.serialize('json', types)
    print response
    return HttpResponse(response)
