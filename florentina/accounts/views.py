from django.shortcuts import render, redirect
from accounts.models import CustomUserForm

def signup(request):
    if request.user.is_authenticated():
        user = request.user.email
        context = {'user':user}
        return render(request, 'accounts/user.html', context )

    form = CustomUserForm()
    context = {'form': form, 'error':''}
    return render(request, 'accounts/signup.html', context)

def create(request):
    user = CustomUserForm(request.POST)
    if not user.is_valid():
        context = {'error':"fuck"}
        return render(request, 'accounts/signup.html', context)
    
    newuser = user.save()
    context = {'user': newuser.email}
    return render(request, 'accounts/user.html', context)
