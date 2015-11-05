from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Flower

def index(request):
    flowers = Flower.objects.all()
    context = {'flowers':flowers}
    return render(request, 'flowers/index.html', context)

def detail(request, id):
    flower = get_object_or_404(Flower, id=id)
    context = {'flower':flower}
    return render(request, 'flowers/detail.html', context)
