# Generated by Django 2.2.12 on 2020-07-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200720_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='flavor_image',
            field=models.ImageField(upload_to='images', verbose_name='フレーバー画像'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='size_image',
            field=models.ImageField(upload_to='images', verbose_name='サイズ画像'),
        ),
    ]
