from django.shortcuts import render
from django.http import HttpResponse

from .models import Flower

def index(request):
    flowers = Flower.objects.all()
    context = {'flowers':flowers}
    return render(request, 'flowers/index.html', context)
