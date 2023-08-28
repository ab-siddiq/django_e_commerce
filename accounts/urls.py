from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register),
    path('profile/',views.profile),
    path('signin/',views.signin),
]
