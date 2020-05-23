from django.urls import path

from library.views import views, form_views

# .../library/
urlpatterns = [
    path('', views.index, name='library-index'),
    path('order/unlisted_add/', form_views.demo, name='demo-form'),
]
