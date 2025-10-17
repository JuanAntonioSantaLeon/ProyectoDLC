from django.contrib import admin

# Register your models here.
from .models import Guest, Stay

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'birth_date']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['birth_date']
    ordering = ("last_name", "first_name")


@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ['guest', 'check_in', 'check_out', 'companions', 'source', 'rating', 'comments']
    search_fields = ['guest__full_name', 'comments']
    list_filter = ['source', 'rating']
    ordering = ("-check_in",)
