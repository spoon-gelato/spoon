# Generated by Django 2.2.12 on 2020-07-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200718_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='flavor2_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='フレーバー2画像'),
        ),
        migrations.AddField(
            model_name='cart',
            name='flavor_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='フレーバー画像'),
        ),
        migrations.AddField(
            model_name='cart',
            name='option2_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='オプション2画像'),
        ),
        migrations.AddField(
            model_name='cart',
            name='option3_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='オプション3画像'),
        ),
        migrations.AddField(
            model_name='cart',
            name='option_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='オプション画像'),
        ),
        migrations.AddField(
            model_name='cart',
            name='size_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='サイズ画像'),
        ),
    ]