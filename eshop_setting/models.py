from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس شرکت')
    phone = models.CharField(max_length=50, verbose_name='شماره ی تماس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    logo_image = models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name='لوگوی شرکت')
    about_us = models.TextField(verbose_name='درباره ی ما')
    copy_right = models.TextField(verbose_name='متن کپی رایت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'بخش تنظیمات'
