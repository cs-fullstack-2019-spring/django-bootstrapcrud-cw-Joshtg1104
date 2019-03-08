from django.urls import path
from . import views

urlpatterns = [
    path('', views.addItem, name='index'),
    path('edit/<int:ID>/', views.editItem, name='edit'),
]
