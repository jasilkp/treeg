from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('client/<int:client_id>/', views.client_details, name='client_details'),
    path('client/<int:client_id>/delete/', views.delete_client, name='delete_client'),

]
