from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from flowers.models import Flower
from accounts.models import CustomUserForm, CustomUserEditForm

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
        context = { 'errors':user.errors }
        return JsonResponse(context)
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
        return JsonResponse(context)

@login_required(login_url='/')
def signout(request):
    logout(request)
    return redirect('flowers:index')

@login_required(login_url='/')
def profile(request):
    if request.method == "POST":
        form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        form.actual_user = request.user 
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        return render(request, 'accounts/profile.html', context)
    else:
        products = request.user.lastSeenProducts.all()[:4]
        userForm = CustomUserEditForm(instance=request.user)
        context = {'form':userForm, 'products': products}
        return render(request, 'accounts/profile.html', context)
