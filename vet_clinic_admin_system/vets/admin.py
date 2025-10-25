from django.contrib import admin
from .models import Vet

@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone",
        "document",
        "crmv",
        "specialty",
        "gender",
        "birth_date",
        "is_active",
        "is_staff",
    )
    list_display_links = ("id", "username", "email")
    list_filter = ("specialty", "gender", "is_active", "is_staff")
    search_fields = ("username", "email", "crmv", "specialty", "document", "phone")
    ordering = ("username",)
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        ("Personal Information", {
            "fields": (
                "username",
                "email",
                "phone",
                "document",
                "birth_date",
                "gender",
                "crmv",
                "specialty",
            )
        }),
        ("Permissions and Access", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Dates", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )