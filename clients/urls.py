from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_client, name='add_client'),
    path('delete/<int:client_id>/', views.delete_client, name='delete_client'),
]
