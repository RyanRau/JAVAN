from django.contrib import admin

from library.models import *


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'isbn', 'category', 'quantity']
    list_display = ('title', 'author', 'isbn', 'category', 'quantity')


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('book', 'user_checkout',
              'checkout_date', 'trello_id')


admin.site.register(Book, BookAdmin)
admin.site.register(Checkout, CheckoutAdmin)
