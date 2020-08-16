from django import forms
from django.core import validators


class CommentForm(forms.Form):
    full_name = forms.CharField(
        validators=[validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواندبیشتر از ۱۵۰ کاراکتر باشد')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}))

    email = forms.EmailField(
        validators=[validators.MaxLengthValidator(150, 'ایمیل شما نمیتواندبیشتر از ۲۰۰ کاراکتر باشد')],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر شما'}))

