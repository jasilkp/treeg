from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_bank_account, name='add_bank_account'),
    path('list/', views.bank_account_list, name='bank_account_list'),
]
