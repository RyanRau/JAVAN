# Generated by Django 2.2.10 on 2020-05-27 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateField(blank=True, null=True)),
                ('checkout_time', models.TimeField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('user_checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_checkout', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
