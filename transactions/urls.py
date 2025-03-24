from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:client_id>/', views.add_transaction, name='add_transaction'),
]
