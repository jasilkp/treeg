from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:client_id>/', views.add_transaction, name='add_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
]
