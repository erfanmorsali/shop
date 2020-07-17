from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    link = models.URLField(verbose_name='لینک')
    image = models.ImageField(upload_to='sliders/', null=True, verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'
