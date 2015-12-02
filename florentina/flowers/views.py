from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Flower
from .models import Category

def index(request):
    category_name = request.GET.get('category','')
    sorting = request.GET.get('sorting', '')
    flowers = Flower.objects.order_by('category')
    # if category is not given, then show all
    if category_name == "":
        context = {'flowers':flowers}
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
    flowers = Flower.objects.filter(category=flower.category).order_by('?')[:4]
    context = {'flower':flower, 'flowers':flowers}
    return render(request, 'flowers/detail.html', context)
