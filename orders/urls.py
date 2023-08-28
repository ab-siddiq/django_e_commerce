from django.urls import path
from . import views

urlpatterns = [
    path('order_completed/',views.order_completed,name='order_completed'),
    path('place_order/',views.place_order,name='placed_order'),
]
