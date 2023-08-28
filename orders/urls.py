from django.urls import path
from . import views

urlpatterns = [
    path('order_completed/',views.order_completed),
]
