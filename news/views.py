# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import News

def index(request):
    news = News.objects.order_by('date')
    context = {'news':news}
    return render(request, 'news/index.html', context)

def detail(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news':news}
    return render(request, 'news/detail.html', context)
