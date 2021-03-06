# Generated by Django 2.2.10 on 2020-05-18 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0009_auto_20200518_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='master_teacher',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(groups__name='Master Teacher'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(4, 'FILLED'), (7, 'RETURNED'), (3, 'UPDATED'), (2, 'PLACED'), (8, 'EMPTIED'), (9, 'DONE'), (0, 'ASSIGNED'), (1, 'STARTED'), (6, 'OUT'), (5, 'SELF-FILLED')], default=0),
        ),
    ]
