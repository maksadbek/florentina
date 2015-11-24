from django.shortcuts import render, redirect
from accounts.models import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core import serializers
from flowers.models import Flower

def signup(request):
    """ create user """
    if request.user.is_authenticated():
        user = request.user.email
        context = {'user':user}
        return redirect('accounts:profile')

    form = CustomUserForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def create(request):
    user = CustomUserForm(request.POST, request.FILES)
    if not user.is_valid():
        context = {'form':user}
        return render(request, 'accounts/signup.html', context)
    else: 
        newuser = user.save()
        newuser.set_password(newuser.password)
        newuser.save()
        return redirect('accounts:profile')

def signin(request):
    """ login user """
    if not request.user.is_authenticated(): 
        return render(request, 'accounts/signin.html')
    return redirect('accounts:profile')

def auth(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return redirect('accounts:profile')
    else:
        context = {'error':'invalid email or password'}
        return render(request, 'accounts/signin.html', context)

def signout(request):
    logout(request)
    return redirect('accounts:signin')

def profile(request):
    if not request.user.is_authenticated():
        return redirect('accounts:signin')
    context = {'user':request.user}
    return render(request, 'accounts/profile.html', context)

def likes(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        flower = get_object_or_404(Flower,postdata['flower_id'])
        request.user.likes.add(flower)
        return HttpResonse("ok")
    elif request.method == 'GET':
        liked_items = request.user.likes.all()
        context = {"likes":liked_items}
        return render(request, 'accounts/likes.html', context)
    elif request.method == 'DELETE':
        flower = get_object_or_404(Flower,request.DELETE['flower_id'])
        request.user.likes.remove(flower)
        return HttpResonse("ok")
