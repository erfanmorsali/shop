# Generated by Django 3.0.8 on 2020-08-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0003_auto_20200827_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='color',
            field=models.CharField(default='آبی', max_length=50, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='size',
            field=models.CharField(default='X', max_length=10, verbose_name='سایز'),
        ),
    ]
