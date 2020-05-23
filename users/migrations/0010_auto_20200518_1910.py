# Generated by Django 2.2.10 on 2020-05-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200518_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='classification',
            field=models.IntegerField(choices=[(4, 'Admin'), (0, 'Student'), (3, 'Master Teacher'), (2, 'Work Study'), (1, 'Mentor')], default=0),
        ),
    ]