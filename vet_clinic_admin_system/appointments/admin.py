from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pet",
        "vet",
        "datetime",
        "status",
        "reason",
        "active",
        "created_at",
    )
    list_display_links = ("id", "pet", "vet")
    list_filter = ("status", "active", "created_at", "vet")
    search_fields = (
        "pet__name",
        "vet__username",
        "vet__email",
        "reason",
    )
    ordering = ("-datetime",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Appointment Details", {
            "fields": (
                "pet",
                "vet",
                "datetime",
                "reason",
                "status",
                "additional_info",
                "active",
            )
        }),
        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )