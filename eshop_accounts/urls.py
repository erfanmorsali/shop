from django.contrib import admin
from django.urls import path, include

from .views import login_page, register_page, log_out

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register', register_page, name='register'),
    path('log_out', log_out, name='log_out'),
]
