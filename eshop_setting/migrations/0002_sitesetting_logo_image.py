# Generated by Django 3.0.8 on 2020-09-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='لوگوی شرکت'),
        ),
    ]
