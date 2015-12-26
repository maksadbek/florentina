# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from .models import Flower, Category, Type
from news.models import News

def index(request):
    category_name = request.GET.get('category','')
    type_name = request.GET.get('type','')
    sorting = request.GET.get('sorting', '')
    flowers_list = Flower.objects.order_by('category')

    news = News.objects.order_by('date')[:1]
    # if category is not given, then show all
    if category_name == "":
        context = {'flowers': flowers_list, 'news': news}
        return render(request, 'flowers/index.html', context)
    # if category is given, filter by category and sort by popularity by default
    if sorting not in ["popularity", "created"]:
        sorting = "popularity"

    page = request.GET.get('page',1)
    category = Category.objects.get(name=category_name)
    try:
        type = Type.objects.get(name=type_name)
    except ObjectDoesNotExist:
        type = Type.objects.first()

    paginator = Paginator(flowers_list.filter(category__name=category_name, type=type).order_by("-"+sorting), 2)

    try:
        flowers = paginator.page(page)
    except PageNotAnInteger:
        flowers = paginator.page(1)
    except EmptyPage:
        flowers = paginator.page(paginator.num_pages)

    context = { 
        'sorting': sorting, 
        'category':category,
        'flowers': flowers,
        'type':type,
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
