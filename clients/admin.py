from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name', 'amount_given', 'deleted', 'deleted_at')
    list_filter = ('deleted',)
    search_fields = ('name', 'project_name')
    readonly_fields = ('deleted', 'deleted_at')