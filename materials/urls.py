from django.urls import path

from materials.views import views, form_views, status_views

# .../materials/
urlpatterns = [
    path('', views.index, name='materials-index'),

    ########################################################################################
    # Urls for editing reservation details
    # /order/(id)/...
    path('order/<int:pk>', views.order_view, name='order-view'),
    path('order/<int:pk>/review', views.order_review, name='order-review'),

    # Status changing of order
    path('order/<int:pk>/status/<int:status_id>/<int:redir>/', status_views.order_status, name='order-status'),


    ############## Forms ################
    # Listed and Unlisted Add
    path('order/listed_add/<int:pk>', form_views.listed_add, name='listed-add'),
    path('order/unlisted_add/', form_views.unlisted_add, name='unlisted-add'),

    # Order Content Edit & Delete
    path('order/content/<int:pk>/edit', form_views.content_edit, name='content-edit'),
    path('order/content/<int:pk>/delete', form_views.content_delete, name='content-delete'),

    # Update pickup information
    path('order/<int:pk>/pickup/update', form_views.pickup_update, name='pickup-update'),

]