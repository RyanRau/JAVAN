# Generated by Django 2.2.10 on 2020-06-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='trello_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]