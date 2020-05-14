# Generated by Django 2.2.10 on 2020-05-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_auto_20200512_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'STARTED'), (8, 'EMPTIED'), (0, 'ASSIGNED'), (5, 'SELF-FILLED'), (4, 'FILLED'), (6, 'OUT'), (2, 'PLACED'), (9, 'DONE'), (7, 'RETURNED'), (3, 'UPDATED')], default=0),
        ),
    ]
