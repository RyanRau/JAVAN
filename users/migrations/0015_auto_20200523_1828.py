# Generated by Django 2.2.10 on 2020-05-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200523_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='classification',
            field=models.IntegerField(choices=[(2, 'Work Study'), (3, 'Master Teacher'), (0, 'Student'), (4, 'Admin'), (1, 'Mentor')], default=0),
        ),
    ]
