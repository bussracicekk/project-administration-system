from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def login_view(request):
    form = LoginForm(request.POST or None,  request.FILES or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        usertype = form.cleaned_data.get('usertype')
        user = authenticate(username=username, password=password, useryype=usertype)
        login(request, user)
        if usertype == "company":
            return redirect('app:homeC')
        if usertype == "customer":
            return redirect('home')
    return render(request, 'accounts/form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('app:homeC')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepassword.html', {
        'form': form
    })
