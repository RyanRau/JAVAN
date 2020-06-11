from django.urls import path

from materials.views import views, form_views, status_views, helpers

# .../materials/
urlpatterns = [
    path('', views.index, name='materials-index'),

    path('browse', views.browse_items, name='browse-items'),

    ########################################################################################
    # Urls for editing reservation details
    # /order/(id)/...
    path('order/<int:pk>', views.order_view, name='order-view'),
    path('order/<int:pk>/review', views.order_review, name='order-review'),

    # Status changing of order
    path('order/<int:pk>/status/<int:status_id>/<int:redir>/', status_views.order_status, name='order-status'),

    ########################################################################################
    # Misc urls
    # Kiosk view
    path('kiosk/', views.kiosk, name='kiosk'),

    # Denied view
    # path('denied/', views.denied, name='denied'),

    ########################################################################################
    # Urls for ajax
    path('items', helpers.item_list, name="item-list"),

    ########################################################################################
    ############## Forms ################
    # Listed and Unlisted Add
    path('order/listed_add/<int:pk>', form_views.listed_add, name='listed-add'),
    path('order/unlisted_add/', form_views.unlisted_add, name='unlisted-add'),

    # Order Content Edit & Delete
    path('order/content/<int:pk>/edit', form_views.content_edit, name='content-edit'),
    path('order/content/<int:pk>/delete', form_views.content_delete, name='content-delete'),

    # Update pickup information
    path('order/<int:pk>/pickup/update', form_views.pickup_update, name='pickup-update'),

    # Item add/edit/delete
    path('item/add', form_views.item_add, name='item-add'),
    path('item/<int:pk>/edit', form_views.item_edit, name='item-edit'),

    ############## Courses ################
    path('course/create', form_views.course_create, name='course-create'),
    path('course/<int:pk>/edit', form_views.course_edit, name='course-edit'),
    # Create new order for course
    path('course/<int:pk>/order/add', form_views.course_order_add, name='course-order-add'),
    path('course/order/<int:pk>/edit', form_views.course_order_edit, name='course-order-edit'),

    # Create new misc order assigned to master teacher
    path('misc/order/add', form_views.misc_order_add, name='misc-order-add'),
    path('misc/order/<int:pk>/edit', form_views.misc_order_edit, name='misc-order-edit'),

]
