# Generated by Django 2.2.12 on 2020-07-15 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_samedayorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SamedayOrder',
            new_name='TodayOrder',
        ),
    ]
