from django.urls import path
from rest_framework.authtoken import views
from .views import index, place_order, login

urlpatterns = [
    path('', index),
    path('order/', place_order, name='order'),
    path('auth/', login)
]
