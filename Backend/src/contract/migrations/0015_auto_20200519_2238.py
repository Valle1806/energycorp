# Generated by Django 3.0.3 on 2020-05-19 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0014_auto_20200519_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 29, 22, 38, 27, 293393)),
        ),
    ]
