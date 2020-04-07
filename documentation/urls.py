from django.urls import path

from . import views

# .../documentation/
urlpatterns = [
    # /
    path('', views.index, name='documentation-index'),

]