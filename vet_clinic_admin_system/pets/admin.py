from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "species",
        "gender",
        "weight",
        "weight_unit",
        "height",
        "height_unit",
        "birth_date",
        "person",
        "active",
        "created_at",
    )
    list_display_links = ("id", "name")
    list_filter = (
        "species",
        "gender",
        "weight_unit",
        "height_unit",
        "active",
        "created_at",
    )
    search_fields = (
        "name",
        "species",
        "person__username",
        "person__email",
    )
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Basic Information", {
            "fields": (
                "name",
                "species",
                "gender",
                "birth_date",
                "person",
                "active",
            )
        }),
        ("Measurements", {
            "fields": (
                "weight",
                "weight_unit",
                "height",
                "height_unit",
            )
        }),
        ("Additional Details", {
            "fields": (
                "additional_info",
                "created_at",
                "updated_at",
            )
        }),
    )