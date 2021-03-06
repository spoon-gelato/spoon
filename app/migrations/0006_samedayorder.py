# Generated by Django 2.2.12 on 2020-07-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_cart_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamedayOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True, help_text='当日注文に対応するかを指定します。 選択を解除すると翌日以降の注文になります。', verbose_name='当日注文')),
            ],
        ),
    ]
