# Generated by Django 2.2.12 on 2020-06-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200624_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='price',
            field=models.IntegerField(null=True, verbose_name='価格'),
        ),
    ]