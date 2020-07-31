from django.urls import path
from users import views

urlpatterns = [
    path('password/', views.change_password, name='change_password'),
    path('signup/', views.signup, name='signup'),
]
