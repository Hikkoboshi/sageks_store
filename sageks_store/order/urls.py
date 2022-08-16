from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('status/', views.order_status, name='order_status')
]