from django.shortcuts import render
from django.contrib import messages
from eshop_setting.models import SiteSetting
from .forms import ContactForm
from .models import ContactUs


# Create your views here.

def contact_us(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        messages.success(request,"پیام شما با موفقت ارسال شد")
        contact_form = ContactForm()
    message = messages.get_messages(request)
    setting = SiteSetting.objects.first()
    context = {
        'setting' : setting ,
        'contact_form': contact_form,
        'message' : message
    }
    return render(request, 'contact_us/contact_us.html', context)
