from django.urls import path
from . import views

urlpatterns = [
    path('AndroidControl/', views.AndroidControl),
    path('getHomeInfo/', views.getHomeInfo),
    path('raspberry/', views.raspberry),
    path('settings/', views.settings),
    path('IRregister/', views.IRregister),
    path('raspOnOff/', views.raspOnOff),

]
