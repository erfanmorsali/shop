from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی نمیتواند بیش از ۱۵۰ کاراکتر باشد')],
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}))

    email = forms.EmailField(
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(150, 'ایمیل شمانمیتواند بیش از ۱۵۰ کاراکتر باشد')],
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'form-control'}))

    subject = forms.CharField(
        label='عنوان پیام',
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام شمانمیتواند بیش از ۲۰۰ کاراکتر باشد')],
        widget=forms.TextInput(attrs={'placeholder': 'عنوان پیام خود را وارد کنید', 'class': 'form-control'}))

    text = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={'placeholder': 'پیام خود را وارد کنید', 'class': 'form-control'}))
