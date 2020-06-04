# Generated by Django 2.2.10 on 2020-05-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0016_auto_20200527_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(6, 'OUT'), (8, 'EMPTIED'), (0, 'ASSIGNED'), (9, 'DONE'), (3, 'UPDATED'), (1, 'STARTED'), (2, 'PLACED'), (5, 'SELF-FILLED'), (7, 'RETURNED'), (4, 'FILLED')], default=0),
        ),
    ]