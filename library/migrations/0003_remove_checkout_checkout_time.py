# Generated by Django 2.2.10 on 2020-05-29 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='checkout_time',
        ),
    ]
