# Generated by Django 2.2.10 on 2020-05-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0011_auto_20200523_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'ASSIGNED'), (7, 'RETURNED'), (9, 'DONE'), (5, 'SELF-FILLED'), (3, 'UPDATED'), (1, 'STARTED'), (6, 'OUT'), (2, 'PLACED'), (4, 'FILLED'), (8, 'EMPTIED')], default=0),
        ),
    ]
