# Generated by Django 2.2.12 on 2020-06-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200627_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavor',
            name='title',
            field=models.CharField(max_length=100, verbose_name='フレーバー'),
        ),
        migrations.AlterField(
            model_name='option',
            name='title',
            field=models.CharField(max_length=100, verbose_name='オプション'),
        ),
    ]