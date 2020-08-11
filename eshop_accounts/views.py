from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, get_user_model


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context[form] = LoginForm()
            if request.user.is_superuser:
                return redirect('http://127.0.0.1:8000/admin/')
            return redirect('/')
        else:
            form.add_error('username', 'کاربری با این مشخصات وجود ندارد')
    return render(request, 'login.html', context)


User = get_user_model()


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        newuser = User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')
    return render(request, 'register.html', context)
