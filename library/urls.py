from django.urls import path

from library.views import views, form_views

# .../library/
urlpatterns = [
    path('', views.index, name='library-index'),
    path('order/unlisted_add/', form_views.demo, name='demo-form'),
    path('books', views.book_list, name='book-list'),
    path('book_details/<int:pk>', form_views.book_details, name='book-details'),
    path('add_book', form_views.add_book, name='add-book'),
    path('book_details/<int:pk>/new_checkout', form_views.new_checkout, name='new-checkout'),
    path('books/<int:pk>/edit', form_views.edit_book, name='edit-book'),
    path('checkouts', views.all_checkouts, name='all-checkouts'),
    path('checkouts/<int:pk>', views.delete_checkout, name='delete-checkout'),
]
