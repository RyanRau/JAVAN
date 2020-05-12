# Generated by Django 2.2.10 on 2020-05-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_auto_20200415_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(4, 'FILLED'), (6, 'OUT'), (1, 'STARTED'), (3, 'UPDATED'), (7, 'RETURNED'), (8, 'EMPTIED'), (9, 'DONE'), (0, 'ASSIGNED'), (2, 'PLACED'), (5, 'SELF-FILLED')], default=0),
        ),
    ]
