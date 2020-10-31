from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, default=None,related_name="cheldren",
                               verbose_name="دسته بندی والد")
    title = models.CharField(max_length=120, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ["parent__id"]
