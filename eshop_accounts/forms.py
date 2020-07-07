from django import forms
from django.core import validators
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}))

    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه ی عبور خود را وارد کنید'}))


class RegisterForm(forms.Form):
    username = forms.CharField(
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='نام کاربری نمیتواند بیش از 20 کاراکتر باشد '),
            validators.MinLengthValidator(limit_value=5, message='نام کاربری نمیتواند کمتر از 5 کاراکتر باشد')
            ],
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}))

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید'}))

    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه ی عبور خود را وارد کنید'}))

    password2 = forms.CharField(
        label=' تکرار کلمه ی عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه ی عبور خود را مجددا وارد کنید'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('کاربری با این ایمیل در سایت موجود میباشد')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('کاربری با این نام کاربری در سایت موجود میباشد')
        return username

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('کلمه های عبور باهم مغایرت دارند')
        return password
