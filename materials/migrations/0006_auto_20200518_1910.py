# Generated by Django 2.2.10 on 2020-05-18 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_auto_20200518_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='master_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(6, 'OUT'), (4, 'FILLED'), (5, 'SELF-FILLED'), (1, 'STARTED'), (0, 'ASSIGNED'), (3, 'UPDATED'), (2, 'PLACED'), (8, 'EMPTIED'), (9, 'DONE'), (7, 'RETURNED')], default=0),
        ),
    ]
