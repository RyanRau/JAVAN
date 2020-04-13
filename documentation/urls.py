from django.urls import path

from . import views

# .../documentation/
urlpatterns = [
    # /
    path('', views.index, name='documentation-index'),
    path('extras/toc', views.view_toc, name="documentation-extras-toc"),
    path('documents/<int:file_id>', views.view_document, name="documentation-view-document")
]