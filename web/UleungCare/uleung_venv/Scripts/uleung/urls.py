from django.urls import path, include
from . import views

urlpatterns = [
    path('AndroidControl/', views.AndroidControl),
    path('getHomeInfo/', views.getHomeInfo),
]
