from django.urls import path

from materials.views import views, form_views

# .../materials/
urlpatterns = [
    path('', views.index, name='materials-index'),

    ########################################################################################
    # Urls for editing reservation details
    # /order/(id)/...
    path('order/<int:pk>', views.order_view, name='order-view'),



    path('order/<int:pk>/pickup/update', form_views.pickup_update, name='pickup-update'),
]