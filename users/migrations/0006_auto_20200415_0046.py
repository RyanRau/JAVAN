# Generated by Django 2.2.10 on 2020-04-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200414_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Mentor'), (4, 'Admin'), (3, 'Master Teacher'), (0, 'Student'), (2, 'Work Study')], default=0),
        ),
    ]
