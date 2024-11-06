from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number',)
    ordering = ('phone_number',)
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password"),
            },
        ),
    )
    search_fields = ( "first_name", "last_name", "phone_number",)
