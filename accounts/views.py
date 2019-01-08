from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login , logout


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        usertype = form.cleaned_data.get('usertype')
        user = authenticate(username=username, password=password, useryype=usertype)
        login(request, user)
        if usertype == "company":
            return redirect('home')
        if usertype == "customer":
            return redirect('home')
    return render(request, 'accounts/form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')