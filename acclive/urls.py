from django.urls import path
from .views import table_view, save_entry, delete_entry

urlpatterns = [
    path('', table_view, name='table'),
    path('save_entry/', save_entry, name='save_entry'),
    path('delete_entry/', delete_entry, name='delete_entry'),
]
