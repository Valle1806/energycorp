# Generated by Django 3.0.3 on 2020-05-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contract', '0001_initial'),
        ('commercial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialinvoice',
            name='invoiceservices',
            field=models.ManyToManyField(related_name='invoiceservices', to='contract.InvoiceServices'),
        ),
    ]
