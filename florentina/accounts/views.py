from django.shortcuts import render, redirect
from accounts.models import CustomUserForm
from django.contrib.auth import authenticate, login, logout

def signup(request):
    """ create user"""
    if request.user.is_authenticated():
        user = request.user.email
        context = {'user':user}
        return redirect('accounts:profile')

    form = CustomUserForm()
    context = {'form': form, 'error':''}
    return render(request, 'accounts/signup.html', context)

def create(request):
    user = CustomUserForm(request.POST, request.FILES)
    if not user.is_valid():
        context = {
            'error':'fuck', 
            'user':user, 
            'validation':user.errors
        }
        return redirect('accounts:signup', context)
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
        return redirect('accounts:signin')

def signout(request):
    logout(request)
    return redirect('accounts:signin')

def profile(request):
    if not request.user.is_authenticated():
        return redirect('accounts:signin')
    context = {'user':request.user}
    return render(request, 'accounts/profile.html', context)
