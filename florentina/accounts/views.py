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
    user = CustomUserForm(request.POST)
    if not user.is_valid():
        context = {'error':'fuck', 'user':user, 'validation':user.errors}
        print user.errors
        print "yes"
        return render(request, 'accounts/signup.html', context)
    else: 
        newuser = user.save()
        newuser.set_password(newuser.password)
        newuser.save()
        context = {'user': newuser.email}
        print "no"
        return render(request, 'accounts/user.html', context)

def signin(request):
    """ login user """
    if not request.user.is_authenticated(): 
        return render(request, 'accounts/signin.html')

    return redirect('accounts:profile')

def auth(request):
    email = request.POST['email']
    password = request.POST['password']
    print email, password

    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        c= {'user', user.email}
        print user.email
        return render(request, 'accounts/user.html')
    else:
        context = {'error':'invalid email or password'}
        return redirect('accounts:signin')

def signout(request):
    logout(request)
    return redirect(request, 'accounts:signin')

def user(request):
    if request.user.is_authenticated():
        context = {'user':request.user.email}
        return render(request, 'accounts/user.html', context)
    else:
        context = {'user':'not authenticated'}
        return render(request, 'accounts/user.html', context)
