from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_client, name='add_client'),
]
