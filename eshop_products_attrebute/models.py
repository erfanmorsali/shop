from django.db import models


# Create your models here.

class ProductAttribute(models.Model):
    size = models.CharField(max_length=10, verbose_name='اندازه')
    color = models.CharField(max_length=50, verbose_name='رنگ')

    class Meta:
        verbose_name = 'مشخصه'
        verbose_name_plural = 'مشخصات'

    def __str__(self):
        return f'{self.size} {self.color}'
