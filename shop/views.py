from django.shortcuts import render, redirect
from eshop_slider.models import Slider

def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'sliders' : sliders
    }
    return render(request, 'home_page.html', context)
