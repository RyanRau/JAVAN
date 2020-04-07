from django.urls import path

from . import views

# .../documentation/
urlpatterns = [
    # /
    path('', views.index, name='documentation-index'),
    path('documents/<str:doc_id>', views.getDocument, name="documentation-get-document")
]