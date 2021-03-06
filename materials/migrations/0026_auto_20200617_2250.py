# Generated by Django 2.2.10 on 2020-06-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0025_auto_20200604_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(9, 'DONE'), (4, 'FILLED'), (8, 'EMPTIED'), (0, 'ASSIGNED'), (7, 'RETURNED'), (5, 'SELF-FILLED'), (3, 'UPDATED'), (6, 'OUT'), (1, 'STARTED'), (2, 'PLACED')], default=0),
        ),
    ]
