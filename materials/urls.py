from django.urls import path

from materials.views import views

# .../materials/
urlpatterns = [
    path('', views.index, name='materials-index'),
]