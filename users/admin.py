from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "profile",
            {
                "fields": (
                    "username",
                    "name",
                    "email",
                    "is_host",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "avatar",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "gender",
                    "language",
                    "currency",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    list_display = ("username", "name", "email")
