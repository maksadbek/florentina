from django.shortcuts import render, redirect
from accounts.models import CustomUserForm, UserFlowers
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

# cart
def cart(request):
    items = request.user.cart.all()
    context = {"cart_items":items}
    return render(request, 'accounts/cart.html', context)

# put flower to cart
def add(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    user_flowers = UserFlowers(user=request.user, flower)
    user_flowers.save()
    cart_items = request.user.cart.all()
    data =serializers.serialize("json",cart_items)
    return HttpResponse(data)

# remove from the cart
def remove(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    request.user.cart.remove(flower)
    cart_items = request.user.cart.all()
    data =serializers.serialize("json",cart_items)
    return HttpResponse(data)
