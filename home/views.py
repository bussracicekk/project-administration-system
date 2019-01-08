from django.shortcuts import render, HttpResponse


def home_view(request):
    #return HttpResponse('<b>Welcome</b>')
    return render(request, 'home/home.html', {})


def company_view(request):
    return render(request, 'home/CompanyHome.html', {})
