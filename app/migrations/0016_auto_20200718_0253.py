# Generated by Django 2.2.12 on 2020-07-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200718_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup',
            name='e_name',
            field=models.CharField(max_length=100, verbose_name='英語名'),
        ),
        migrations.AlterField(
            model_name='pickup',
            name='j_name',
            field=models.CharField(max_length=100, verbose_name='日本語名'),
        ),
    ]