# Generated by Django 2.2.12 on 2020-07-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200716_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=0, verbose_name='注文番号'),
        ),
    ]
