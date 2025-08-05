from django.urls import path 
from . import views
urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('/lokasi', views.lokasi, name='lokasi'),
    path('lokasi/delete/<int:lid>/', views.delete_lokasi, name='delete_lokasi'),
    path('/e1', views.e1, name='e1'),
]