from django.contrib import admin
from .models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
