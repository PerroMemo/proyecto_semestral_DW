from django.shortcuts import render

# Create your views here.

def index(request):

    context = {}
    return render(request, 'app/index.html',context)


def about_us(request):

    context = {}
    return render(request, 'app/about_us.html',context)

def login(request):

    context = {}
    return render(request, 'app/login.html',context)

def registro(request):

    context = {}
    return render(request, 'app/registro.html',context)

def error(request):

    context = {}
    return render(request, 'app/error.html',context)