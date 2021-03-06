from datetime import timedelta, datetime, date

from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    user_checkout = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_checkout',
        null=False
    )
    checkout_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    trello_id = models.CharField(max_length=50, blank=True)

    @property
    def is_over_due(self):
        return date.today() > self.return_date




