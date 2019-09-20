from django.urls import path, include
from . import views

urlpatterns = [
    path('androidControl/', views.androidControl),
]
