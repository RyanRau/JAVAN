# Generated by Django 2.2.10 on 2020-05-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200415_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='classification',
            field=models.IntegerField(choices=[(4, 'Admin'), (0, 'Student'), (3, 'Master Teacher'), (1, 'Mentor'), (2, 'Work Study')], default=0),
        ),
    ]