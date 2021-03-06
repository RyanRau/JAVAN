# Generated by Django 2.2.10 on 2020-06-23 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_checkout_trello_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.Book'),
            preserve_default=False,
        ),
    ]
