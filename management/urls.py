from django.urls import path

from management.views import views
from management.views.materials import api_views, form_views


# .../management/
urlpatterns = [
    path('', views.index, name='management-index'),

    # Order
    path('orders/', views.order_list, name='management-order-list'),
    path('orders/<int:pk>', views.order_view, name='management-order-view'),

    path('orders/api/order-search', api_views.order_search, name='management-api-order-search'),

    path('orders/forms/order-details-edit/<int:pk>', form_views.order_details_edit,  name='management-forms-order-details'),


    # Course
    path('courses/', views.course_list, name='management-course-list'),
    path('courses/<int:pk>', views.course_view, name='management-course-view'),

    path('courses/api/course-search', api_views.course_search, name='management-api-course-search'),
]
