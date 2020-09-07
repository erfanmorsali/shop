from django.shortcuts import render, redirect

from eshop_setting.models import SiteSetting
from eshop_slider.models import Slider


def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer(request):
    setting = SiteSetting.objects.first()
    context = {
        'setting': setting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'sliders': sliders
    }
    return render(request, 'home_page.html', context)


def about_us(request):
    contents = SiteSetting.objects.all().last()
    context = {
        "contents": contents
    }
    return render(request, 'about_page.html', context)
