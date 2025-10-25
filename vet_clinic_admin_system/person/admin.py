from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

@admin.register(Person)
class PersonAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone",
        "document",
        "gender",
        "birth_date",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_display_links = ("id", "username", "email")
    list_filter = ("gender", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "email", "phone", "document")
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
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "document",
                "phone",
                "password1",
                "password2",
                "is_active",
                "is_staff",
            ),
        }),
    )