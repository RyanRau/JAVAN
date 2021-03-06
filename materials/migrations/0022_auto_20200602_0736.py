# Generated by Django 2.2.10 on 2020-06-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0021_auto_20200528_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(6, 'OUT'), (8, 'EMPTIED'), (7, 'RETURNED'), (5, 'SELF-FILLED'), (2, 'PLACED'), (0, 'ASSIGNED'), (9, 'DONE'), (4, 'FILLED'), (3, 'UPDATED'), (1, 'STARTED')], default=0),
        ),
    ]
