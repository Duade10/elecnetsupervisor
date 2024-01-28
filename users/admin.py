from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_supervisor",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            "Customer User Fields",
            {
                "fields": (
                    "is_supervisor",
                )
            },
        ),
    )

    search_fields = (
        "first_name__icontains",
        "first_name",
        "last_name__icontains",
        "email__icontains",
    )

    ordering = ("email",)
