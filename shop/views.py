from django.shortcuts import render, redirect


def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    context = {}
    return render(request, 'home_page.html', context)
